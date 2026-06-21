def bfs_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return None
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    if start == end:
        return [start]
    queue = [(start, [start])]
    visited = set()
    visited.add(start)
    while queue:
        (current, path) = queue.pop(0)
        cx, cy = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) not in visited and grid[nx][ny] == 0:
                    new_path = path + [(nx, ny)]
                    if (nx, ny) == end:
                        return new_path
                    visited.add((nx, ny))
                    queue.append(((nx, ny), new_path))
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    sample_start = (0, 0)
    sample_end = (3, 3)
    result = bfs_shortest_path(sample_grid, sample_start, sample_end)
    print(result)