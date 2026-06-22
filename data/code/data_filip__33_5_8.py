import heapq

def find_minimum_cost_path(grid):
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start_pos = None
    start_val = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != -1:
                start_pos = (r, c)
                start_val = grid[r][c]
                break
        if start_pos:
            break
    
    if not start_pos:
        return -1
    
    start_r, start_c = start_pos
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start_r][start_c] = start_val
    
    pq = [(start_val, start_r, start_c)]
    
    while pq:
        current_dist, r, c = heapq.heappop(pq)
        
        if current_dist > distances[r][c]:
            continue
        
        if r == rows - 1 and c == cols - 1:
            return current_dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                weight = grid[nr][nc]
                new_dist = current_dist + weight
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))
    
    return distances[rows - 1][cols - 1] if distances[rows - 1][cols - 1] != float('inf') else -1

if __name__ == '__main__':
    sample_grid = [
        [0, 2, 1, 4],
        [1, 3, -1, 2],
        [5, 4, 1, 1],
        [3, 6, 2, 0]
    ]
    result = find_minimum_cost_path(sample_grid)
    print(result)