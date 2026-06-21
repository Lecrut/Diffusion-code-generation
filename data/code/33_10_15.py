import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
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
        
        if current in closed_set:
            continue
        
        closed_set.add(current)
        
        r, c = current
        neighbors = [
            (r - 1, c), (r + 1, c),
            (r, c - 1), (r, c + 1),
            (r - 1, c - 1), (r - 1, c + 1),
            (r + 1, c - 1), (r + 1, c + 1)
        ]
        
        for neighbor in neighbors:
            nr, nc = neighbor
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if neighbor in closed_set:
                    continue
                
                move_cost = 1.414 if abs(nr - r) == 1 and abs(nc - c) == 1 else 1
                tentative_g = g_score.get(current, float('inf')) + move_cost
                
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
    
    return []

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
    path = astar_search(grid, start, goal)
    print(path)