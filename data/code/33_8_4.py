import collections

def validate_grid(grid):
    if not grid:
        raise ValueError("Grid cannot be empty")
    row_len = len(grid[0])
    if row_len == 0:
        raise ValueError("Grid rows cannot be empty")
    for i, row in enumerate(grid):
        if len(row) != row_len:
            raise ValueError("Grid is not rectangular")
        for j, cell in enumerate(row):
            if cell not in (0, 1, 2, 3):
                raise ValueError(f"Invalid cell value at ({i}, {j})")
    return len(grid), row_len

def validate_points(rows, cols, start, end):
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        raise ValueError(f"Start point {start} out of bounds for grid size {rows}x{cols}")
    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        raise ValueError(f"End point {end} out of bounds for grid size {rows}x{cols}")

def bfs_shortest_path(grid, start, end):
    rows, cols = validate_grid(grid)
    validate_points(rows, cols, start, end)
    
    if grid[start[0]][start[1]] != 0:
        raise ValueError("Start point is not a walkable cell")
    if grid[end[0]][end[1]] != 0:
        raise ValueError("End point is not a walkable cell")

    queue = collections.deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (r, c), path = queue.popleft()
        
        if (r, c) == end:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] != 1:
                    visited.add((nr, nc))
                    new_path = list(path)
                    new_path.append((nr, nc))
                    queue.append(((nr, nc), new_path))
    
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0]
    ]
    
    start_point = (0, 0)
    end_point = (4, 4)
    
    result = bfs_shortest_path(sample_grid, start_point, end_point)
    print(result)