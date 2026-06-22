from collections import deque

def shortest_path(grid):
    if not grid or not grid[0]:
        return []
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                if start is None:
                    start = (r, c)
                end = (r, c)
            else:
                grid[r][c] = 1
    if start is None or end is None:
        return []
    if start == end:
        return [start]
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        (r, c), path = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                new_path = path + [(nr, nc)]
                if (nr, nc) == end:
                    return new_path
                visited.add((nr, nc))
                queue.append(((nr, nc), new_path))
    return []

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0]
    ]
    result = shortest_path(sample_grid)
    print(result)