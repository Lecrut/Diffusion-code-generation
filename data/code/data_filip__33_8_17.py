from collections import deque

def bfs_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if rows == 0 or cols == 0:
        return None

    if not isinstance(start, (list, tuple)) or len(start) != 2:
        return None
    if not isinstance(end, (list, tuple)) or len(end) != 2:
        return None

    r1, c1 = start
    r2, c2 = end

    if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols:
        return None
    if r2 < 0 or r2 >= rows or c2 < 0 or c2 >= cols:
        return None

    if grid[r1][c1] == 1 or grid[r2][c2] == 1:
        return None

    if r1 == r2 and c1 == c2:
        return [(r1, c1)]

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(r1, c1, [(r1, c1)])])
    visited[r1][c1] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, path = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                new_path = path + [(nr, nc)]
                if nr == r2 and nc == c2:
                    return new_path
                visited[nr][nc] = True
                queue.append((nr, nc, new_path))

    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]
    ]
    start_point = (0, 0)
    end_point = (3, 3)
    result = bfs_shortest_path(sample_grid, start_point, end_point)
    print(result)