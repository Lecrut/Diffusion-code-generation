from collections import deque

def bfs_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if not grid or not all(len(row) == cols for row in grid):
        raise ValueError("Invalid grid: rows have inconsistent lengths")

    r_start, c_start = start
    r_end, c_end = end

    if not (0 <= r_start < rows and 0 <= c_start < cols):
        raise ValueError("Start point out of bounds")
    if not (0 <= r_end < rows and 0 <= c_end < cols):
        raise ValueError("End point out of bounds")
    if grid[r_start][c_start] == 1:
        raise ValueError("Start point is blocked")
    if grid[r_end][c_end] == 1:
        raise ValueError("End point is blocked")

    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None

def validate_and_find_path(grid, start, end):
    try:
        return bfs_shortest_path(grid, start, end)
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    sample_start = (0, 0)
    sample_end = (4, 4)

    result = validate_and_find_path(sample_grid, sample_start, sample_end)
    print(result)

    invalid_grid = [
        [0, 1],
        [0, 1, 0]
    ]
    invalid_result = validate_and_find_path(invalid_grid, (0, 0), (1, 2))
    print(invalid_result)

    blocked_start_grid = [
        [1, 0],
        [0, 0]
    ]
    blocked_result = validate_and_find_path(blocked_start_grid, (0, 0), (1, 1))
    print(blocked_result)