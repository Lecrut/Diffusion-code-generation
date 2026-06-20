def detect_cycles(graph):
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
        if not node in visited and dfs(node):
            return True
    return False

if __name__ == '__main__':
    sample_graph = {
        'A': ['B'],
        'B': ['C', 'E'],
        'C': ['D'],
        'D': ['F'],
        'E': [],
        'F': ['C']
    }
    print(detect_cycles(sample_graph))