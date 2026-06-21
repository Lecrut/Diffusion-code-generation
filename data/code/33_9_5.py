import heapq

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.terrain = [[False] * width for _ in range(height)]

    def walkable(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and not self.terrain[y][x]

    def cost(self, current, neighbor):
        dx = neighbor[0] - current[0]
        dy = neighbor[1] - current[1]
        return 1.0 if dx != 0 and dy != 0 else 1.0

    def neighbors(self, node):
        x, y = node
        dirs = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0),           (1, 0),
            (-1, 1),  (0, 1), (1, 1)
        ]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if self.walkable(nx, ny):
                yield (nx, ny)

def heuristic(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return dx + dy + (1.41421356 - 2) * min(dx, dy)

def astar(grid, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    open_set_hash = {start}
    
    while open_set:
        current_f, current = heapq.heappop(open_set)
        open_set_hash.discard(current)
        
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in grid.neighbors(current):
            tentative_g = g_score[current] + grid.cost(current, neighbor)
            
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, end)
                f_score[neighbor] = f
                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f, neighbor))
                    open_set_hash.add(neighbor)
    return None

if __name__ == '__main__':
    grid = Grid(10, 10)
    grid.terrain[3][2] = True
    grid.terrain[3][3] = True
    grid.terrain[3][4] = True
    
    start_node = (0, 0)
    end_node = (9, 9)
    
    path = astar(grid, start_node, end_node)
    
    total_cost = 0
    for i in range(1, len(path)):
        total_cost += grid.cost(path[i-1], path[i])
    
    print(path)
    print(total_cost)