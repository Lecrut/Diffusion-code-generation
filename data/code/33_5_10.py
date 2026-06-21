import heapq

def min_cost_path(grid):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[0][0] = grid[0][0]
    heap = [(grid[0][0], 0, 0)]
    while heap:
        cost, r, c = heapq.heappop(heap)
        if r == rows - 1 and c == cols - 1:
            return cost
        if cost > distances[r][c]:
            continue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = cost + grid[nr][nc]
                if new_cost < distances[nr][nc]:
                    distances[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))
    return distances[rows - 1][cols - 1]

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = min_cost_path(sample_grid)
    print(result)