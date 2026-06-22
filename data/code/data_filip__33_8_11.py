import collections

def is_valid(grid, point):
    if not grid:
        return False
    rows = len(grid)
    if rows == 0:
        return False
    cols = len(grid[0])
    r, c = point
    if r < 0 or r >= rows:
        return False
    if c < 0 or c >= cols:
        return False
    if grid[r][c] == 1:
        return False
    return True

def bfs_shortest_path(grid, start, end):
    if not grid or not start or not end:
        return None
    rows = len(grid)
    cols = len(grid[0])
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return None
    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return None
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    if start == end:
        return [start]
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        (curr_r, curr_c), path = queue.popleft()
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                new_path = path + [(nr, nc)]
                if (nr, nc) == end:
                    return new_path
                visited.add((nr, nc))
                queue.append(((nr, nc), new_path))
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 1]
    ]
    sample_start = (0, 0)
    sample_end = (3, 2)
    result = bfs_shortest_path(sample_grid, sample_start, sample_end)
    print(result)