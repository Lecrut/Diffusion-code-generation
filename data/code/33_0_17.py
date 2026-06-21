from collections import deque

def shortest_path(grid):
    if not grid or not grid[0]:
        return []
    rows = len(grid)
    cols = len(grid[0])
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return None
    queue = deque([(0, 0, [(0, 0)])])
    visited = set([(0, 0)])
    while queue:
        r, c, path = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return path
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, path + [(nr, nc)]))
    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    result = shortest_path(grid)
    print(result)