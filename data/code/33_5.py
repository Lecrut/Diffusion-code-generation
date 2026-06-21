import heapq

def find_min_cost_path(grid):
    if not grid or not grid[0]:
        return float('inf'), []
    
    rows = len(grid)
    cols = len(grid[0])
    
    dist = [[float('inf')] * cols for _ in range(rows)]
    prev = [[None] * cols for _ in range(rows)]
    
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        
        if r == rows - 1 and c == cols - 1:
            path = []
            curr = (r, c)
            while curr is not None:
                path.append(curr)
                curr = prev[curr[0]][curr[1]]
            path.reverse()
            return d, path
        
        if d > dist[r][c]:
            continue
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = d + grid[nr][nc]
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    prev[nr][nc] = (r, c)
                    heapq.heappush(pq, (new_dist, nr, nc))
    
    return float('inf'), []

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    cost, path = find_min_cost_path(sample_grid)
    print(cost)
    print(path)