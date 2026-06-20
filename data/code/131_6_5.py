def has_cycle(graph):
    visited = set()
    recursive_visited = set()

    def dfs(node):
        if node in recursive_visited:
            return True
        if node in visited:
            return False
        visited.add(node)
        recursive_visited.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        recursive_visited.remove(node)
        return False
    for node in graph:
        if node not in visited and dfs(node):
            return True
    return False
if __name__ == '__main__':
    sample_graph = {'A': ['B'], 'B': ['C', 'E'], 'C': ['D'], 'D': ['A'], 'E': []}
    print(has_cycle(sample_graph))