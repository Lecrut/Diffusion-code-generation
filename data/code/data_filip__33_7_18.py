from collections import deque

def bfs_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return -1
        
    if start == end:
        return 0
        
    queue = deque([(start, 0)])
    visited = set([start])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (r, c), dist = queue.popleft()
        
        if (r, c) == end:
            return dist
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
                
    return -1

if __name__ == '__main__':
    grid_example = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_example = (0, 0)
    end_example = (4, 4)
    
    result = bfs_shortest_path(grid_example, start_example, end_example)
    print(result)