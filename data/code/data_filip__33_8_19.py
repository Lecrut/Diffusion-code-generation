from collections import deque

def is_valid(grid, r, c):
    rows = len(grid)
    if rows == 0:
        return False
    cols = len(grid[0])
    if c < 0 or c >= cols:
        return False
    return r >= 0 and r < rows and grid[r][c] != 1

def shortest_path(grid, start, end):
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    start_r, start_c = start
    end_r, end_c = end
    
    if not is_valid(grid, start_r, start_c):
        raise ValueError("Start point is invalid or blocked")
    if not is_valid(grid, end_r, end_c):
        raise ValueError("End point is invalid or blocked")
    
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    queue.append((start_r, start_c, 0))
    visited = set()
    visited.add((start_r, start_c))
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == end_r and c == end_c:
            return dist
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and is_valid(grid, nr, nc):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    sample_start = (0, 0)
    sample_end = (2, 3)
    result = shortest_path(sample_grid, sample_start, sample_end)
    print(result)