from collections import deque
import heapq

def shortest_path_grid(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return None
        
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return None
        
    if start == end:
        return 0
    
    queue = deque([(start, 0)])
    visited = set([start])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        (r, c), dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) == end:
                    return dist + 1
                if grid[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
                    
    return None

def shortest_path_grid_weighted(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return float('inf')
        
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return float('inf')
        
    if start == end:
        return grid[start[0]][start[1]]
    
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    heap = [(grid[0][0], 0, 0)]
    visited = set([(0, 0)])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while heap:
        d, r, c = heapq.heappop(heap)
        
        if (r, c) == end:
            return d
            
        if d > dist[r][c]:
            continue
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = d + grid[nr][nc]
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    if (nr, nc) not in visited:
                        heapq.heappush(heap, (new_dist, nr, nc))
                        
    return float('inf')

if __name__ == '__main__':
    grid_unweighted = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    grid_weighted = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    result_unweighted = shortest_path_grid(grid_unweighted)
    print(result_unweighted)
    
    result_weighted = shortest_path_grid_weighted(grid_weighted)
    print(result_weighted)