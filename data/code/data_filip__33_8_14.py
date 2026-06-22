from collections import deque

def validate_grid(grid):
    if not grid:
        return True, None
    if not grid[0]:
        return True, None
    rows = len(grid)
    cols = len(grid[0])
    for row in grid:
        if len(row) != cols:
            raise ValueError("Grid is not rectangular")
    return True, (rows, cols)

def validate_points(grid, start, end):
    valid, dimensions = validate_grid(grid)
    if not valid:
        raise ValueError("Invalid grid")
    
    rows, cols = dimensions
    
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        raise ValueError("Start point out of bounds")
        
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        raise ValueError("End point out of bounds")
        
    if grid[start[0]][start[1]] == 1:
        raise ValueError("Start point is blocked")
        
    if grid[end[0]][end[1]] == 1:
        raise ValueError("End point is blocked")
        
    return True

def bfs_shortest_path(grid, start, end):
    validate_points(grid, start, end)
    
    rows, cols = len(grid), len(grid[0])
    
    if start == end:
        return 0
    
    visited = set()
    visited.add(start)
    queue = deque([(start, 0)])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (r, c), dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) == end:
                    return dist + 1
                    
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
                    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 1]
    ]
    
    sample_start = (0, 0)
    sample_end = (2, 3)
    
    result = bfs_shortest_path(sample_grid, sample_start, sample_end)
    print(result)