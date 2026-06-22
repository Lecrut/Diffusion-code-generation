from collections import deque

def min_steps_to_exit(grid, start, exit_pos):
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    start_r, start_c = start
    end_r, end_c = exit_pos

    if grid[start_r][start_c] == 1 or grid[end_r][end_c] == 1:
        return -1

    if start == exit_pos:
        return 0

    visited = [[False] * cols for _ in range(rows)]
    visited[start_r][start_c] = True

    queue = deque([(start_r, start_c, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, dist = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) == (end_r, end_c):
                    return dist + 1
                
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

    return -1

if __name__ == '__main__':
    grid_sample = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    start_point = (0, 0)
    exit_point = (3, 3)
    result = min_steps_to_exit(grid_sample, start_point, exit_point)
    print(result)