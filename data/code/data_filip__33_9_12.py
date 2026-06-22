import heapq
import math

def astar_grid(grid, start, goal, allow_diagonal=True):
    rows = len(grid)
    cols = len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        current_f, current = heapq.heappop(open_set)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        if current_f > f_score.get(current, float('inf')):
            continue
        
        neighbors = get_neighbors(current, rows, cols, allow_diagonal)
        
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue
            
            tentative_g = g_score[current] + distance(current, neighbor, allow_diagonal)
            
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                f_score[neighbor] = f
                heapq.heappush(open_set, (f, neighbor))
    
    return None

def heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def distance(a, b, allow_diagonal):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    if dx + dy == 0:
        return 0
    if dx == 0 or dy == 0:
        return dx + dy
    if allow_diagonal:
        return min(dx, dy) * math.sqrt(2) + abs(dx - dy)
    return dx + dy

def get_neighbors(pos, rows, cols, allow_diagonal):
    neighbors = []
    r, c = pos
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    if not allow_diagonal:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    
    return neighbors

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

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
    path = astar_grid(grid, start, goal, allow_diagonal=True)
    print(path)