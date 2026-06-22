import heapq

def astar(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    
    g_score = {}
    g_score[start] = 0
    
    f_score = {}
    f_score[start] = heuristic(start, end)
    
    while open_set:
        current_f, current = heapq.heappop(open_set)
        
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        if current_f > f_score.get(current, float('inf')):
            continue
            
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            
            nr, nc = neighbor
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            
            if grid[nr][nc] == 1:
                continue
            
            tentative_g = g_score[current] + 1
            
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, end)
                f_score[neighbor] = f
                heapq.heappush(open_set, (f, neighbor))
                
    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    result = astar(grid, start_node, end_node)
    print(result)