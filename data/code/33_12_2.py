import heapq

def dijkstra(grid, start, end):
    rows = len(grid)
    if rows == 0:
        return float('inf'), []
    cols = len(grid[0])
    
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return float('inf'), []
    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return float('inf'), []
    if grid[start[0]][start[1]] == float('inf'):
        return float('inf'), []
    if grid[end[0]][end[1]] == float('inf'):
        return float('inf'), []

    dist = [[float('inf')] * cols for _ in range(rows)]
    prev = [[None] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0
    
    pq = [(0, start[0], start[1])]
    visited = set()
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        if (r, c) == end:
            break
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                weight = grid[nr][nc]
                if weight == float('inf'):
                    continue
                
                new_dist = d + weight
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
    grid = [
        [1, 3, 1, 1],
        [1, 5, 1, 4],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    
    start_node = (0, 0)
    end_node = (3, 3)
    
    cost, path = dijkstra(grid, start_node, end_node)
    
    print(cost)
    print(path)