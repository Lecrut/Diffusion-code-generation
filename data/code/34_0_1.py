import heapq

def a_star_grid(start, goal, obstacles, grid_rows=10, grid_cols=10):
    if start in obstacles or goal in obstacles:
        return None
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    rows = range(grid_rows)
    cols = range(grid_cols)
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    closed_set = set()
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        closed_set.add(current)
        
        neighbors = [
            (current[0] - 1, current[1]),
            (current[0] + 1, current[1]),
            (current[0], current[1] - 1),
            (current[0], current[1] + 1)
        ]
        
        for next_node in neighbors:
            if not (0 <= next_node[0] < grid_rows and 0 <= next_node[1] < grid_cols):
                continue
            if next_node in obstacles:
                continue
            if next_node in closed_set:
                continue
            
            tentative_g = g_score[current] + 1
            
            if next_node not in g_score or tentative_g < g_score[next_node]:
                came_from[next_node] = current
                g_score[next_node] = tentative_g
                f_score = tentative_g + heuristic(next_node, goal)
                heapq.heappush(open_set, (f_score, next_node))
    
    return None

if __name__ == '__main__':
    obstacles = {(2, 2), (2, 3), (2, 4)}
    start_pos = (0, 0)
    goal_pos = (5, 5)
    result = a_star_grid(start_pos, goal_pos, obstacles)
    print(result)