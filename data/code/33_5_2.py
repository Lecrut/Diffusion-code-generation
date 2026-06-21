import heapq

def minimum_cost_path(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    if rows == 1 and cols == 1:
        return grid[0][0]
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    visited = [[False] * cols for _ in range(rows)]
    dist = [[float('inf')] * cols for _ in range(rows)]
    
    dist[0][0] = grid[0][0]
    
    pq = [(grid[0][0], 0, 0)]
    
    while pq:
        cost, r, c = heapq.heappop(pq)
        
        if r == rows - 1 and c == cols - 1:
            return cost
        
        if visited[r][c]:
            continue
        
        visited[r][c] = True
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                new_cost = cost + grid[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
    
    return dist[rows - 1][cols - 1]

if __name__ == '__main__':
    grid = [
        [5, 4, 8],
        [1, 1, 5],
        [3, 2, 1]
    ]
    result = minimum_cost_path(grid)
    print(result)