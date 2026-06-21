from collections import deque

def shortest_path_bfs(grid, start, end):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return None
    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return None
    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return None
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True
    queue = deque()
    queue.append((start[0], start[1], 0))
    while queue:
        r, c, dist = queue.popleft()
        if r == end[0] and c == end[1]:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    return None

if __name__ == '__main__':
    grid = [
        [1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 1, 1, 1, 1]
    ]
    start = (0, 0)
    end = (4, 4)
    result = shortest_path_bfs(grid, start, end)
    print(result)