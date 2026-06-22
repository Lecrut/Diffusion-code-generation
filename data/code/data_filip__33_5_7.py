import heapq

def min_cost_path(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    
    pq = [(grid[0][0], 0, 0)]
    
    while pq:
        cost, r, c = heapq.heappop(pq)
        
        if cost > dist[r][c]:
            continue
        
        if r == rows - 1 and c == cols - 1:
            return cost
        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = cost + grid[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
                    
    return dist[rows - 1][cols - 1]

if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = min_cost_path(grid)
    print(result)