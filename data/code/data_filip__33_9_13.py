import heapq
import math

def heuristic(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    
    neighbors = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    closed_set = set()
    
    while open_set:
        current_f, current = heapq.heappop(open_set)
        
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path
        
        if current in closed_set:
            continue
            
        closed_set.add(current)
        
        for dr, dc in neighbors:
            neighbor = (current[0] + dr, current[1] + dc)
            
            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                continue
                
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue
                
            if neighbor in closed_set:
                continue
                
            move_cost = math.sqrt(2) if (dr != 0 and dc != 0) else 1
            tentative_g = g_score.get(current, float('inf')) + move_cost
            
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

def create_sample_grid():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0]
    ]
    return grid

def run_sample():
    grid = create_sample_grid()
    start = (0, 0)
    goal = (7, 7)
    
    path = astar(grid, start, goal)
    
    if path is None:
        return []
    
    path_values = []
    for pos in path:
        path_values.append(grid[pos[0]][pos[1]])
    
    return path

if __name__ == '__main__':
    result = run_sample()
    print(result)