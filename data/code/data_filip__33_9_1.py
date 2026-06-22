import heapq
import math

def heuristic(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
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
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            data.append(start)
            data.reverse()
            return data
        
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
            
            if (dr, dc) in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                movement_cost = math.sqrt(2)
                if grid[current[0]][current[1]] == 0 and grid[neighbor[0]][neighbor[1]] == 0:
                    if grid[current[0] + (dr if abs(dr) > 0 else 0)][current[1]] == 1 and grid[current[0]][current[1] + (dc if abs(dc) > 0 else 0)] == 1:
                        continue
            else:
                movement_cost = 1
            
            tentative_g = g_score[current] + movement_cost
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    path = astar(grid, start, goal)
    print(path)