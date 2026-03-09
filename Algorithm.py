from collections import deque
import math
class Algorithm:
    def __init__(self):
        self.graph = {
            'A': [('B', 4), ('C', 2), ('D', 7)],
            'B': [('E', 3), ('F', 6)],
            'C': [('F', 1), ('G', 9)],
            'D': [('G', 2)],
            'E': [('H', 5)],
            'F': [('H', 2), ('I', 4)],
            'G': [('I', 1)],
            'H': [('J', 3)],
            'I': [('J', 6)],
            'J': []
            }
        self.cost = 0
    
    def search(self):
        queue = deque()
        self.path = []
        visited = set()
        curr = 'A'
        queue.append(curr)

        while len(queue) > 0:
            curr_weight = math.inf
            curr = queue.popleft()
            self.path.append(curr)
            if not self.graph[curr]: return
            
            for node, weight in self.graph[curr]:
                    if node not in visited:
                        if weight < curr_weight:
                            curr_weight = weight
                            curr = node
            
            queue.append(curr)
            visited.add(curr)
            self.cost += curr_weight
    
    def print_path(self):
        print("--------------------------------------------------")
        print("Final Path: ")
        for node in self.path:
            if node == self.path[len(self.path) - 1]:
                print(node, end="\n")
            else:
                print(node, end=" -> ")
        print("Total cost: " + str(self.cost))
        print("--------------------------------------------------")






    