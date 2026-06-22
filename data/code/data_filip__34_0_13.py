import heapq

def a_star_shortest_path(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start))
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
            return path[::-1]
        
        closed_set.add(current)
        
        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            r, c = neighbor
            
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and neighbor not in closed_set:
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
    
    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    goal = (4, 4)
    path = a_star_shortest_path(grid, start, goal)
    print(path)