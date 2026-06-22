from collections import deque

def shortest_path(grid):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                start = (r, c)
            elif grid[r][c] == 3:
                end = (r, c)
    if start is None or end is None:
        return None
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_path = path + [(nr, nc)]
                    queue.append(((nr, nc), new_path))
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 1, 0, 0]
    ]
    sample_grid[0][0] = 2
    sample_grid[3][3] = 3
    result = shortest_path(sample_grid)
    print(result)