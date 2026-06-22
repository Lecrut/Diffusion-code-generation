import heapq
import math

def get_neighbors(node, grid_width, grid_height):
    x, y = node
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_width and 0 <= ny < grid_height:
                cost = 1.0 if dx == 0 or dy == 0 else math.sqrt(2)
                neighbors.append(((nx, ny), cost))
    return neighbors

def heuristic(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)

def a_star(grid_width, grid_height, start, end):
    if start == end:
        return [start], 0
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    
    while open_set:
        current_f, current = heapq.heappop(open_set)
        
        if current == end:
            path = []
            total_cost = g_score[end]
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, total_cost
        
        for neighbor, weight in get_neighbors(current, grid_width, grid_height):
            tentative_g_score = g_score[current] + weight
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return [], 0

if __name__ == '__main__':
    width = 10
    height = 10
    start_node = (0, 0)
    end_node = (9, 9)
    
    path, cost = a_star(width, height, start_node, end_node)
    
    print(path)
    print(cost)