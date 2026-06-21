from collections import deque

def find_shortest_path(grid, start, end):
    if not grid or not isinstance(grid, list):
        raise ValueError("Invalid grid")
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if cols == 0:
        raise ValueError("Grid columns must be greater than zero")
    
    for row in grid:
        if len(row) != cols:
            raise ValueError("Grid rows must have equal length")
    
    if not isinstance(start, tuple) or len(start) != 2:
        raise ValueError("Start must be a tuple of two integers")
    
    if not isinstance(end, tuple) or len(end) != 2:
        raise ValueError("End must be a tuple of two integers")
    
    sr, sc = start
    er, ec = end
    
    if not (0 <= sr < rows and 0 <= sc < cols):
        raise ValueError("Start point out of bounds")
    
    if not (0 <= er < rows and 0 <= ec < cols):
        raise ValueError("End point out of bounds")
    
    if grid[sr][sc] == 0:
        raise ValueError("Start point is blocked")
    
    if grid[er][ec] == 0:
        raise ValueError("End point is blocked")
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    queue.append((sr, sc, 0))
    visited[sr][sc] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == (er, ec):
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 1, 1, 1]
    ]
    sample_start = (0, 0)
    sample_end = (3, 3)
    
    result = find_shortest_path(sample_grid, sample_start, sample_end)
    print(result)