class Graph:

    def __init__(self):
        self.graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}

    def has_cycle(self, vertex, visited=None, recursion_stack=None):
        if visited is None:
            visited = set()
        if recursion_stack is None:
            recursion_stack = set()
        visited.add(vertex)
        recursion_stack.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if self.has_cycle(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True
        recursion_stack.remove(vertex)
        return False
if __name__ == '__main__':
    graph = Graph()
    print(graph.has_cycle('A'))