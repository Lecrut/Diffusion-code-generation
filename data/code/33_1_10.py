import heapq

def shortest_path_on_grid(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return None
    
    if start == end:
        return [start]
    
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    
    visited = set()
    dist = {start: 0}
    prev = {start: None}
    heap = [(0, start)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while heap:
        current_dist, current_pos = heapq.heappop(heap)
        
        if current_pos in visited:
            continue
        
        visited.add(current_pos)
        
        if current_pos == end:
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = prev[node]
            return path[::-1]
        
        r, c = current_pos
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbor = (nr, nc)
                
                if neighbor not in visited and grid[nr][nc] == 0:
                    new_dist = current_dist + 1
                    
                    if neighbor not in dist or new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        prev[neighbor] = current_pos
                        heapq.heappush(heap, (new_dist, neighbor))
    
    return None

if __name__ == '__main__':
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    result = shortest_path_on_grid(grid, start, end)
    print(result)