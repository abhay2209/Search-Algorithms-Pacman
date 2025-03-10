# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 25-30
It would have been less if I had more experience with Python, the challenge for me was to use Python in a complex manner.
Though this won't be an issue for further assignments.
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
The course theory is way easier than the assignments. I understood well about the concepts, yet it was super had to implement it in the assignment
It was fun though doing this assignment, took me about a 5 days of work (5 hours a day atleast). If more about the implementation is taught, 
the class discusses only theory. I was blank while doing the assignment. I had to spend hours skimming through the book for helpful facts.

"""
#####################################################
#####################################################

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    You will get (5,5)

    print (problem.isGoalState(problem.getStartState()) )
    You will get True
   
    print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
    """First we make sure that the start state is not same as the goal state """
    if problem.isGoalState(problem.getStartState()):
        return [] 

    """As we need LIFO for DFS"""
    from util import Stack
    """"Now I have to initialize frontier with the initial state of the problem, according to fig 3.7"""
    Frontier = Stack()
    """Now I push the valid start state"""
    Frontier.push((problem.getStartState(),[]))
    """initializing empty explored set"""
    statePath=[]
    stateVisited=[]
    while(True):
        """return failure if Frontier is empty """
        if Frontier.isEmpty():
            return []
        """choose a leaf node and remove it from Frontier"""    
        xy,statePath = Frontier.pop() 
        """ if it is the goal state, return it"""
        if problem.isGoalState(xy):
            return statePath
        """Add the node to the explored set"""    
        stateVisited.append(xy)
        """expand the chosen node """
        succecorPath = problem.getSuccessors(xy) 
        """print ( problem.getSuccessors(xy)), test for successor """
        if succecorPath:
            for paths in succecorPath:
                """Adding resulting nodes in Frontier only if not in frontier or explored set """
                if paths[0] not in stateVisited :  
                    newPath = statePath + [paths[1]] 
                    """
                    print(paths[0])
                    print(paths[1])
                    print(newPath) """
                    Frontier.push((paths[0],newPath))
 
    
        



def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """The code is same as Depth First search, but we use Queue instead of Stack """
    if problem.isGoalState(problem.getStartState()):
        return [] 

    """As we need FIFO for DFS"""
    from util import Queue
    """"Now I have to initialize frontier with the initial state of the problem, according to fig 3.7"""
    Frontier = Queue()
    """Now I push the valid start state"""
    Frontier.push((problem.getStartState(),[]))
    """initializing empty explored set"""
    statePath=[]
    stateVisited=[]
    while(True):
        """return failure if Frontier is empty """
        if Frontier.isEmpty():
            return []
        """choose a leaf node and remove it from Frontier"""    
        xy,statePath = Frontier.pop() 
        """ if it is the goal state, return it"""
        if problem.isGoalState(xy):
            return statePath
        """Add the node to the explored set"""    
        stateVisited.append(xy)
        """expand the chosen node """
        succecorPath = problem.getSuccessors(xy) 
        """print ( problem.getSuccessors(xy)), test for successor """
        if succecorPath:
            for paths in succecorPath:
                """Adding resulting nodes in Frontier only if not in frontier or explored set """
                if paths[0] not in stateVisited and paths[0] not in (state[0] for state in Frontier.list): 
                    """A condtion is added in the above if, we had to check all the nodes where we have been (states) """
                    newPath = statePath + [paths[1]] 
                    """
                    print(paths[0])
                    print(paths[1])
                    print(newPath) """
                    Frontier.push((paths[0],newPath))
    



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return [] 

    """As we need LIFO for DFS"""
    from util import PriorityQueue
    """ Initiliazing state of the problem"""
    Frontier = PriorityQueue()        
    """Pushing valid start state (this time we also have to consider priorities """            
    Frontier.push(problem.getStartState(),0)
    """Initializing empty explored set """
    statePath=[]  
    stateVisited = []                                
    tempPath=[]     
    """ Choosing a leaf node to remove it from Frontier"""                            
    xy = Frontier.pop() 
    """Initilaizing one more priority Queue for the path to our current """                                   
    pathCurrent=PriorityQueue()  
    """Running the loop until we are not in goal state """             
    while not problem.isGoalState(xy):
        """Not a  previosly visited node """
        if xy not in stateVisited:
            stateVisited.append(xy)
            """Getting Successors """
            successorPath = problem.getSuccessors(xy)
            """This is where a major change occurs comapred to other two searches, so to clearly illustrate i used them individually instead of 'paths' """
            for coordinate,direction,cost in successorPath:
                newPath = statePath + [direction]
                """ Getting cost of path with state in hand"""
                costOfPath = problem.getCostOfActions(newPath) + heuristic(coordinate,problem)
                """
                print(costOfPath)"""
                if coordinate not in stateVisited:
                    """
                    print(direction)
                    print(coordinate)
                    """
                    Frontier.push(coordinate,costOfPath)
                    pathCurrent.push(newPath,costOfPath)
        xy = Frontier.pop()
        statePath = pathCurrent.pop()    
    return statePath
    
   

    

def priorityQueueDepthFirstSearch(problem):
    """
    Q1.4a.
    Reimplement DFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return [] 

    """As we need LIFO for DFS"""
    from util import PriorityQueue
    """"Now I have to initialize frontier with the initial state of the problem, according to fig 3.7"""
    Frontier = PriorityQueue()
    """Now I push the valid start state"""
    Frontier.push((problem.getStartState(),[]),0)
    """initializing empty explored set"""
    statePath=[]
    stateVisited=[]
    i=10000
    while(True):
        """return failure if Frontier is empty """
        if Frontier.isEmpty():
            return []
        """choose a leaf node and remove it from Frontier"""    
        xy,statePath = Frontier.pop() 
        """ if it is the goal state, return it"""
        if problem.isGoalState(xy):
            return statePath
        """Add the node to the explored set"""    
        stateVisited.append(xy)
        """expand the chosen node """
        succecorPath = problem.getSuccessors(xy) 
        """Special thanks to Piaza discussions """
        succecorPath.reverse() 
        i=i-1
        """print ( problem.getSuccessors(xy)), test for successor """
        if succecorPath:
            
            for paths in succecorPath:
                
                """Adding resulting nodes in Frontier only if not in frontier or explored set """
                if paths[0] not in stateVisited :  
                    newPath = statePath + [paths[1]] 
                    
                    """
                    print(paths[0])
                    print(paths[1])
                    print(newPath) """
                    Frontier.push((paths[0],newPath),i)
                    
                    
    
  


def priorityQueueBreadthFirstSearch(problem):
    """
    Q1.4b.
    Reimplement BFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return [] 

    """As we need LIFO for DFS"""
    from util import PriorityQueue
    """"Now I have to initialize frontier with the initial state of the problem, according to fig 3.7"""
    Frontier = PriorityQueue()
    """Now I push the valid start state"""
    Frontier.push((problem.getStartState(),[]),0)
    """initializing empty explored set"""
    statePath=[]
    stateVisited=[]
    
    while(True):
        """return failure if Frontier is empty """
        if Frontier.isEmpty():
            return []
        """choose a leaf node and remove it from Frontier"""    
        xy,statePath = Frontier.pop() 
        """ if it is the goal state, return it"""
        if problem.isGoalState(xy):
            return statePath
        """Add the node to the explored set"""    
        stateVisited.append(xy)
        """expand the chosen node """
        succecorPath = problem.getSuccessors(xy) 
        i=-1
        """print ( problem.getSuccessors(xy)), test for successor """
        if succecorPath:
            for paths in succecorPath:
                """Adding resulting nodes in Frontier only if not in frontier or explored set """
                if paths[0] not in stateVisited :  
                    newPath = statePath + [paths[1]] 
                    
                    """
                    print(paths[0])
                    print(paths[1])
                    print(newPath) """
                    
                    Frontier.push((paths[0],newPath),i)
                    i=i-1

#####################################################
#####################################################
# Discuss the results of comparing the priority-queue
# based implementations of BFS and DFS with your original
# implementations.

"""
for BFS 
mediumMazeNode expanded are a little more with priority-queue
bigMazeNode expanded are a little less

for DFS it's same
This concludes that nodes expanded are same for DFS, but when we do BFS nodes are expanded differently in both cases.
Maybe this was the result was of the functioning.As queue works in FIFO and priority queue assign weight to nodes thus a different order for inseertion and extraction.
"""



#####################################################
#####################################################



# Abbreviations (please DO NOT change these.)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bfs2 = priorityQueueBreadthFirstSearch
dfs2 = priorityQueueDepthFirstSearch