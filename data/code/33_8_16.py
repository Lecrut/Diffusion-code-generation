from collections import deque

def validate_grid_inputs(grid, start, end):
    if not isinstance(grid, list) or not all(isinstance(row, list) for row in grid):
        raise ValueError("Grid must be a 2D list")
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    rows = len(grid)
    cols = len(grid[0])
    for i, row in enumerate(grid):
        if len(row) != cols:
            raise ValueError(f"Row {i} has inconsistent length")
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        raise ValueError(f"Start point {start} is out of grid bounds")
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        raise ValueError(f"End point {end} is out of grid bounds")
    if grid[start[0]][start[1]] == 1:
        raise ValueError("Start point is blocked")
    if grid[end[0]][end[1]] == 1:
        raise ValueError("End point is blocked")

def bfs_shortest_path(grid, start, end):
    validate_grid_inputs(grid, start, end)
    rows = len(grid)
    cols = len(grid[0])
    queue = deque([(start, [start])])
    visited = set()
    visited.add(tuple(start))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]
    ]
    sample_start = (0, 0)
    sample_end = (3, 3)
    result = bfs_shortest_path(sample_grid, sample_start, sample_end)
    print(result)