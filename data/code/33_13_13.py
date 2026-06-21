import collections

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

    queue = collections.deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        current_dist = dist[r][c]

        if r == n - 1 and c == n - 1:
            return current_dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                new_dist = current_dist + 1
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    queue.append((nr, nc))

    return -1

if __name__ == '__main__':
    grid1 = [
        [0, 1],
        [1, 0]
    ]
    print(shortestPathBinaryMatrix(grid1))

    grid2 = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(shortestPathBinaryMatrix(grid2))

    grid3 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(shortestPathBinaryMatrix(grid3))