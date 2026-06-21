import heapq
import math

def heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    closed_set = set()
    
    while open_set:
        current_f, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        closed_set.add(current)
        
        cr, cc = current
        neighbors = []
        
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbors.append((nr, nc))
        
        for neighbor in neighbors:
            nr, nc = neighbor
            
            if neighbor in closed_set:
                continue
            
            if grid[nr][nc] == 1:
                continue
            
            dr = nr - cr
            dc = nc - cc
            
            if abs(dr) + abs(dc) == 2:
                move_cost = math.sqrt(2)
                if grid[cr][nc] == 1 or grid[nr][cc] == 1:
                    continue
            else:
                move_cost = 1
            
            tentative_g = g_score[current] + move_cost
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                if neighbor not in closed_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return []

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    path = astar(grid, start, goal)
    print(path)