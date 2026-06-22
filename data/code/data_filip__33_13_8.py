from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1
    if n == 1:
        return 1

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 1
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        current_dist = dist[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                new_dist = current_dist + 1
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    queue.append((nr, nc))

    return dist[n - 1][n - 1] if dist[n - 1][n - 1] != float('inf') else -1

if __name__ == '__main__':
    grid_sample = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 0]
    ]
    result = shortestPathBinaryMatrix(grid_sample)
    print(result)

    grid_sample2 = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    result2 = shortestPathBinaryMatrix(grid_sample2)
    print(result2)

    grid_sample3 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    result3 = shortestPathBinaryMatrix(grid_sample3)
    print(result3)