import heapq

def shortest_path_on_grid(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return []
    
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []
    
    if start == end:
        return [start]
    
    distance = [[float('inf')] * cols for _ in range(rows)]
    distance[start[0]][start[1]] = 0
    previous = [[None] * cols for _ in range(rows)]
    
    pq = [(0, start)]
    visited = set()
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while pq:
        current_dist, (r, c) = heapq.heappop(pq)
        
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        if (r, c) == end:
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = previous[current[0]][current[1]]
            return path[::-1]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and distance[nr][nc] == float('inf') and (nr, nc) not in visited:
                distance[nr][nc] = current_dist + 1
                previous[nr][nc] = (r, c)
                heapq.heappush(pq, (current_dist + 1, (nr, nc)))
    
    return []

if __name__ == '__main__':
    grid_sample = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    result = shortest_path_on_grid(grid_sample, start_point, end_point)
    print(result)