import heapq

class GridMap:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles)

    def get_neighbors(self, point):
        x, y = point
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                if (nx, ny) not in self.obstacles:
                    neighbors.append((nx, ny))
        return neighbors

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: grid.heuristic(start, goal)}
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
        
        if current in closed_set:
            continue
        closed_set.add(current)
        
        for neighbor in grid.get_neighbors(current):
            if neighbor in closed_set:
                continue
            
            tentative_g_score = g_score[current] + 1
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f = tentative_g_score + grid.heuristic(neighbor, goal)
                f_score[neighbor] = f
                heapq.heappush(open_set, (f, neighbor))
    
    return None

if __name__ == '__main__':
    obstacles = [(2, 2), (3, 2), (4, 2), (5, 2)]
    grid = GridMap(10, 10, obstacles)
    start = (0, 0)
    goal = (9, 9)
    path = a_star(grid, start, goal)
    print(path)