from collections import deque

def shortest_path_bfs(grid, start, end):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    if start == end:
        return 0
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return -1
    queue = deque([(start, 0)])
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        (r, c), dist = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                if (nr, nc) == end:
                    return dist + 1
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    return -1

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start = (0, 0)
    end = (3, 3)
    result = shortest_path_bfs(grid, start, end)
    print(result)