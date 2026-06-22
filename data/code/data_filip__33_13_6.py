def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1
    if n == 1:
        return 1
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 1
    import heapq
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    pq = [(1, 0, 0)]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    while pq:
        d, x, y = heapq.heappop(pq)
        if x == n - 1 and y == n - 1:
            return d
        for dx, dy in directions:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < n and (not visited[nx][ny]) and (grid[nx][ny] == 0):
                visited[nx][ny] = True
                heapq.heappush(pq, (d + 1, nx, ny))
    return -1
if __name__ == '__main__':
    grid1 = [[0, 1], [1, 0]]
    print(shortest_path_binary_matrix(grid1))
    grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(shortest_path_binary_matrix(grid2))
    grid3 = [[1, 0], [0, 0]]
    print(shortest_path_binary_matrix(grid3))