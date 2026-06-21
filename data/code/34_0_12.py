import heapq

def a_star_search(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    open_set_hash = {start}
    
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while open_set:
        current_f, current = heapq.heappop(open_set)
        open_set_hash.discard(current)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for i, j in moves:
            neighbor_row = current[0] + i
            neighbor_col = current[1] + j
            
            if not (0 <= neighbor_row < rows and 0 <= neighbor_col < cols):
                continue
            
            if grid[neighbor_row][neighbor_col] == 1:
                continue
            
            tentative_g_score = g_score[current] + 1
            
            neighbor = (neighbor_row, neighbor_col)
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    open_set_hash.add(neighbor)
    
    return None

if __name__ == '__main__':
    grid_data = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start_pos = (0, 0)
    goal_pos = (4, 4)
    
    result = a_star_search(grid_data, start_pos, goal_pos)
    print(result)