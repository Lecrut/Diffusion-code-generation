import heapq

def shortest_path_dijkstra(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    start_r, start_c = start
    end_r, end_c = end
    
    if grid[start_r][start_c] == 0 or grid[end_r][end_c] == 0:
        return None
    
    visited = set()
    visited.add((start_r, start_c))
    
    pq = [(grid[start_r][start_c], start_r, start_c)]
    dist = {(start_r, start_c): grid[start_r][start_c]}
    parent = {(start_r, start_c): None}
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pq:
        current_dist, r, c = heapq.heappop(pq)
        
        if (r, c) == (end_r, end_c):
            path = []
            curr = (end_r, end_c)
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return path
        
        if current_dist > dist.get((r, c), float('inf')):
            continue
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != 0:
                new_dist = current_dist + grid[nr][nc]
                if (nr, nc) not in dist or new_dist < dist[(nr, nc)]:
                    dist[(nr, nc)] = new_dist
                    parent[(nr, nc)] = (r, c)
                    heapq.heappush(pq, (new_dist, nr, nc))
                visited.add((nr, nc))
                
    return None

if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    start_pos = (0, 0)
    end_pos = (4, 4)
    result = shortest_path_dijkstra(grid, start_pos, end_pos)
    print(result)