def bfs_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if not grid or not any(grid):
        return []

    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return []

    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return []

    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []

    from collections import deque

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return []

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]
    ]
    sample_start = (0, 0)
    sample_end = (3, 3)

    result = bfs_shortest_path(sample_grid, sample_start, sample_end)
    print(result)