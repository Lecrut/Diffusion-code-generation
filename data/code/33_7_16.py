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
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    queue.append((start, [start]))
    visited[start[0]][start[1]] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        for dr, dc in directions:
            r = current[0] + dr
            c = current[1] + dc
            if 0 <= r < rows and 0 <= c < cols and not visited[r][c] and grid[r][c] == 0:
                visited[r][c] = True
                queue.append(((r, c), path + [(r, c)]))
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_pos = (0, 0)
    end_pos = (4, 4)
    result = shortest_path_bfs(sample_grid, start_pos, end_pos)
    print(result)