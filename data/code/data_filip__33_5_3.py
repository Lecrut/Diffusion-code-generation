import heapq
import sys

def find_minimum_cost_path(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    min_heap = [(grid[0][0], 0, 0)]
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    
    while min_heap:
        current_cost, r, c = heapq.heappop(min_heap)
        
        if r == rows - 1 and c == cols - 1:
            return current_cost
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = True
                new_cost = current_cost + grid[nr][nc]
                heapq.heappush(min_heap, (new_cost, nr, nc))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    
    result = find_minimum_cost_path(sample_grid)
    print(result)