import heapq

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    open_set_hash = {start}
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current not in open_set_hash:
            continue
        
        open_set_hash.discard(current)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for dr, dc in directions:
            neighbor_r = current[0] + dr
            neighbor_c = current[1] + dc
            neighbor = (neighbor_r, neighbor_c)
            
            if not (0 <= neighbor_r < rows and 0 <= neighbor_c < cols):
                continue
            
            if grid[neighbor_r][neighbor_c] == 1:
                continue
            
            tentative_g = g_score[current] + 1
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                
                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    open_set_hash.add(neighbor)
                    
    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)
    
    result = astar(grid, start, goal)
    print(result)