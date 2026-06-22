import heapq

def find_min_cost_path(grid):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    heap = [(grid[0][0], 0, 0)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while heap:
        cost, r, c = heapq.heappop(heap)
        if r == rows - 1 and c == cols - 1:
            return cost
        if cost > dist[r][c]:
            continue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = cost + grid[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))
    return float('inf')

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = find_min_cost_path(sample_grid)
    print(result)