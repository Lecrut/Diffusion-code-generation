import heapq

def min_cost_path(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    
    if rows == 1 and cols == 1:
        return grid[0][0]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    
    while pq:
        current_dist, r, c = heapq.heappop(pq)
        
        if visited[r][c]:
            continue
        visited[r][c] = True
        
        if r == rows - 1 and c == cols - 1:
            return current_dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                new_dist = current_dist + grid[nr][nc]
                
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))
                    
    return dist[rows - 1][cols - 1]

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = min_cost_path(sample_grid)
    print(result)