import heapq
import math

def dijkstra_grid(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> tuple[list[int], tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])
    
    dist = [[math.inf] * cols for _ in range(rows)]
    prev = [[None] * cols for _ in range(rows)]
    
    sr, sc = start
    er, ec = end
    
    if sr < 0 or sr >= rows or sc < 0 or sc >= cols:
        return [], (sr, sc)
        
    if er < 0 or er >= rows or ec < 0 or ec >= cols:
        return [], (sr, sc)
        
    dist[sr][sc] = grid[sr][sc]
    
    pq = [(grid[sr][sc], sr, sc)]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        
        if d > dist[r][c]:
            continue
            
        if (r, c) == (er, ec):
            break
            
        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]
        
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols:
                weight = grid[nr][nc]
                new_dist = d + weight
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    prev[nr][nc] = (r, c)
                    heapq.heappush(pq, (new_dist, nr, nc))
                    
    if dist[er][ec] == math.inf:
        return [], (er, ec)
        
    path = []
    curr = (er, ec)
    while curr is not None:
        path.append(curr)
        curr = prev[curr[0]][curr[1]]
        
    path.reverse()
    
    return [dist[er][ec]], (er, ec)

if __name__ == '__main__':
    grid_data = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    start_node = (0, 0)
    end_node = (2, 2)
    
    result = dijkstra_grid(grid_data, start_node, end_node)
    print(result)