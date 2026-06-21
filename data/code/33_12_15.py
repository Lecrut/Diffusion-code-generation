import heapq

def dijkstra(grid):
    rows = len(grid)
    cols = len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    if rows == 0 or cols == 0:
        return float('inf')
    
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = grid[0][0]
    
    visited = set()
    heap = [(distances[0][0], 0, 0)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while heap:
        current_dist, r, c = heapq.heappop(heap)
        
        if (r, c) in visited:
            continue
        
        visited.add((r, c))
        
        if (r, c) == end:
            return current_dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    new_dist = current_dist + grid[nr][nc]
                    if new_dist < distances[nr][nc]:
                        distances[nr][nc] = new_dist
                        heapq.heappush(heap, (new_dist, nr, nc))
    
    return float('inf')

if __name__ == '__main__':
    grid_sample = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = dijkstra(grid_sample)
    print(result)