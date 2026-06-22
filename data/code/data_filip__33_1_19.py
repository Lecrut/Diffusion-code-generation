import heapq

def get_neighbors(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid_neighbors = []
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
            valid_neighbors.append((nr, nc))
    return valid_neighbors

def shortest_path_dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, (r, c) = heapq.heappop(priority_queue)
        
        if (r, c) == end:
            return current_dist
        
        if current_dist > distances[r][c]:
            continue
        
        for nr, nc in get_neighbors(grid, r, c):
            weight = grid[nr][nc] if isinstance(grid[nr][nc], (int, float)) else 1
            distance = current_dist + weight
            
            if distance < distances[nr][nc]:
                distances[nr][nc] = distance
                heapq.heappush(priority_queue, (distance, (nr, nc)))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    result = shortest_path_dijkstra(sample_grid, start_node, end_node)
    print(result)