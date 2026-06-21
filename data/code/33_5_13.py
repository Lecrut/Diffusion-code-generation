import heapq

def min_cost_path(grid):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    heap = [(grid[0][0], 0, 0)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while heap:
        d, r, c = heapq.heappop(heap)
        if d > dist[r][c]:
            continue
        if r == rows - 1 and c == cols - 1:
            return d
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = d + grid[nr][nc]
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(heap, (new_dist, nr, nc))
    return -1

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = min_cost_path(sample_grid)
    print(result)