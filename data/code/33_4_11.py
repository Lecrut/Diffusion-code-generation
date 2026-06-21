import collections

def bidirectional_bfs(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return None
    
    if start == end:
        return [start]
    
    start_r, start_c = start
    end_r, end_c = end
    
    if (not 0 <= start_r < rows or not 0 <= start_c < cols or
        not 0 <= end_r < rows or not 0 <= end_c < cols):
        return None
    
    if grid[start_r][start_c] == 1 or grid[end_r][end_c] == 1:
        return None
    
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    start_visited = {start: None}
    end_visited = {end: None}
    
    start_queue = collections.deque([start])
    end_queue = collections.deque([end])
    
    while start_queue and end_queue:
        if len(start_queue) <= len(end_queue):
            current_queue = start_queue
            current_visited = start_visited
            other_visited = end_visited
        else:
            current_queue = end_queue
            current_visited = end_visited
            other_visited = start_visited
        
        current = current_queue.popleft()
        
        cr, cc = current
        
        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                
                if neighbor not in current_visited:
                    current_visited[neighbor] = current
                    current_queue.append(neighbor)
                    
                    if neighbor in other_visited:
                        path = []
                        node = neighbor
                        while node is not None:
                            path.append(node)
                            node = current_visited[node]
                        path.reverse()
                        
                        node = other_visited[neighbor]
                        while node is not None:
                            path.append(node)
                            node = other_visited[node]
                        
                        return path
    
    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    end = (4, 4)
    
    path = bidirectional_bfs(grid, start, end)
    print(path)
    
    grid2 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    
    start2 = (0, 0)
    end2 = (2, 2)
    
    path2 = bidirectional_bfs(grid2, start2, end2)
    print(path2)
    
    grid3 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    
    start3 = (0, 0)
    end3 = (0, 2)
    
    path3 = bidirectional_bfs(grid3, start3, end3)
    print(path3)
    
    grid4 = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    
    start4 = (0, 0)
    end4 = (2, 2)
    
    path4 = bidirectional_bfs(grid4, start4, end4)
    print(path4)
    
    grid5 = [
        [0]
    ]
    
    start5 = (0, 0)
    end5 = (0, 0)
    
    path5 = bidirectional_bfs(grid5, start5, end5)
    print(path5)