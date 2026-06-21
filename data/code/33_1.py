import heapq
from typing import List, Tuple, Optional

def dijkstra_grid(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[float, List[Tuple[int, int]]]:
    rows = len(grid)
    if rows == 0:
        raise ValueError("Grid is empty")
    cols = len(grid[0])
    if cols == 0:
        raise ValueError("Grid has no columns")
    
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        raise ValueError("Start position is out of bounds")
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        raise ValueError("End position is out of bounds")
    if grid[start[0]][start[1]] == -1:
        raise ValueError("Start position is an obstacle")
    if grid[end[0]][end[1]] == -1:
        raise ValueError("End position is an obstacle")
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0
    
    prev = [[None] * cols for _ in range(rows)]
    
    pq = [(0, start[0], start[1])]
    visited = [[False] * cols for _ in range(rows)]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        
        if visited[r][c]:
            continue
        visited[r][c] = True
        
        if (r, c) == end:
            break
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] != -1:
                new_dist = d + grid[nr][nc]
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    prev[nr][nc] = (r, c)
                    heapq.heappush(pq, (new_dist, nr, nc))
    
    if dist[end[0]][end[1]] == float('inf'):
        return float('inf'), []
    
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = prev[curr[0]][curr[1]]
    path.reverse()
    
    return dist[end[0]][end[1]], path

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1, 1],
        [1, -1, 1, 4],
        [2, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    start_pos = (0, 0)
    end_pos = (3, 3)
    
    distance, shortest_path = dijkstra_grid(sample_grid, start_pos, end_pos)
    print(distance)
    print(shortest_path)