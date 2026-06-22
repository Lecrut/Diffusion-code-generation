import collections

def shortest_path_binary_matrix(grid):
    if not grid or not grid[0]:
        return -1
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1
    if n == 1:
        return 1
    queue = collections.deque([(0, 0, 1)])
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                if nr == n - 1 and nc == n - 1:
                    return dist + 1
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(shortest_path_binary_matrix(sample_grid))