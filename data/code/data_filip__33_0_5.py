from collections import deque

def bfs_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return None

    rows = len(grid)
    cols = len(grid[0])
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return None
    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return None

    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None

    queue = deque([(start[0], start[1], [start])])
    visited = set((start[0], start[1]))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, path = queue.popleft()
        if (r, c) == end:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                new_path = list(path)
                new_path.append((nr, nc))
                queue.append((nr, nc, new_path))

    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    result = bfs_shortest_path(grid, start, end)
    print(result)