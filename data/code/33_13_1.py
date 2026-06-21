import heapq

def shortest_path_binary_matrix(grid):
    if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    n, m = len(grid), len(grid[0])
    if n == 1 and m == 1:
        return 1
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 1
    heap = [(1, 0, 0)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    while heap:
        d, i, j = heapq.heappop(heap)
        if d > dist[i][j]:
            continue
        if i == n - 1 and j == m - 1:
            return d
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0:
                new_dist = d + 1
                if new_dist < dist[ni][nj]:
                    dist[ni][nj] = new_dist
                    heapq.heappush(heap, (new_dist, ni, nj))
    return -1

if __name__ == '__main__':
    grid1 = [[0, 1], [1, 0]]
    print(shortest_path_binary_matrix(grid1))
    grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(shortest_path_binary_matrix(grid2))
    grid3 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(shortest_path_binary_matrix(grid3))