from collections import deque

def shortest_path(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1
    start = (0, 0)
    end = (rows - 1, cols - 1)
    queue = deque([(start, 0)])
    visited = {start}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        (r, c), dist = queue.popleft()
        if (r, c) == end:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    return -1

if __name__ == '__main__':
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    print(shortest_path(grid))