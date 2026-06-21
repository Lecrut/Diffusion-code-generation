from collections import deque

def validate_and_solve(grid, start, end):
    if not grid or not isinstance(grid, list):
        raise ValueError("Grid must be a non-empty list of lists")
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if cols == 0 or any(len(row) != cols for row in grid):
        raise ValueError("Grid must be rectangular and non-empty")
    
    sr, sc = start
    er, ec = end
    
    if not (0 <= sr < rows and 0 <= sc < cols):
        raise ValueError("Start point is out of bounds")
    if not (0 <= er < rows and 0 <= ec < cols):
        raise ValueError("End point is out of bounds")
    if grid[sr][sc] == 1:
        raise ValueError("Start point is blocked")
    if grid[er][ec] == 1:
        raise ValueError("End point is blocked")
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[sr][sc] = True
    queue = deque([(sr, sc, 0)])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        r, c, dist = queue.popleft()
        if r == er and c == ec:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    grid_sample = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start_sample = (0, 0)
    end_sample = (3, 3)
    result = validate_and_solve(grid_sample, start_sample, end_sample)
    print(result)