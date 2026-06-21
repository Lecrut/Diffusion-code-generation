import heapq

def minimum_cost_path(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    pq = [(dist[0][0], 0, 0)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while pq:
        current_cost, r, c = heapq.heappop(pq)
        if r == rows - 1 and c == cols - 1:
            return current_cost
        if current_cost > dist[r][c]:
            continue
        for dr, dc in directions:
            nr, nc = (r + dr, c + dc)
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = current_cost + grid[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
    return dist[rows - 1][cols - 1]
if __name__ == '__main__':
    sample_grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = minimum_cost_path(sample_grid)
    print(result)