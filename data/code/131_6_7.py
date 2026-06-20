def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            return True
        if node in visited:
            return False
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        rec_stack.remove(node)
        return False
    for node in graph:
        if not visited and dfs(node):
            return True
    return False
if __name__ == '__main__':
    graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []}
    print(has_cycle(graph))