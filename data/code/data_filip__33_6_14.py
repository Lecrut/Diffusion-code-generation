import collections

def shortest_path(grid):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    queue = collections.deque()
    queue.append((0, 0, 1))
    visited = set()
    visited.add((0, 0))
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while queue:
        r, c, dist = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    result = shortest_path(sample_grid)
    print(result)