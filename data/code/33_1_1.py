import heapq

def get_neighbors(r, c, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def dijkstra(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if not (0 <= start[0] < rows and 0 <= start[1] < cols) or grid[start[0]][start[1]] == 1:
        return None
    if not (0 <= end[0] < rows and 0 <= end[1] < cols) or grid[end[0]][end[1]] == 1:
        return None
    
    distances = {}
    predecessors = {}
    pq = []
    
    for r in range(rows):
        for c in range(cols):
            distances[(r, c)] = float('inf')
            predecessors[(r, c)] = None
    
    distances[start] = 0
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        if current == end:
            break
        
        for neighbor in get_neighbors(current[0], current[1], rows, cols):
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue
            
            weight = 1
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))
    
    if distances[end] == float('inf'):
        return None
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    result_path = dijkstra(grid, start_node, end_node)
    print(result_path)