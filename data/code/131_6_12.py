class GraphCycles:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def has_cycle_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        for neighbor in self.adjacency_list[v]:
            if not visited[neighbor]:
                if self.has_cycle_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[v] = False
        return False

    def has_cycle(self):
        visited = {node: False for node in self.adjacency_list}
        rec_stack = {node: False for node in self.adjacency_list}
        for node in self.adjacency_list:
            if not visited[node]:
                if self.has_cycle_util(node, visited, rec_stack):
                    return True
        return False
if __name__ == '__main__':
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': ['C'], 'E': [], 'F': []}
    gc = GraphCycles(graph)
    print(gc.has_cycle())