import heapq
from typing import List, Tuple, Optional

def find_minimum_cost_path(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[int]:
    if not grid or not grid[0]:
        return None
    
    rows = len(grid)
    cols = len(grid[0])
    start_r, start_c = start
    end_r, end_c = end
    
    if not (0 <= start_r < rows and 0 <= start_c < cols):
        return None
    if not (0 <= end_r < rows and 0 <= end_c < cols):
        return None
    
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start_r][start_c] = grid[start_r][start_c]
    
    heap = [(grid[start_r][start_c], start_r, start_c)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while heap:
        current_dist, r, c = heapq.heappop(heap)
        
        if current_dist > distances[r][c]:
            continue
        
        if r == end_r and c == end_c:
            return current_dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = current_dist + grid[nr][nc]
                
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    heapq.heappush(heap, (new_dist, nr, nc))
    
    return None

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    start_node = (0, 0)
    end_node = (2, 2)
    
    result = find_minimum_cost_path(sample_grid, start_node, end_node)
    print(result)