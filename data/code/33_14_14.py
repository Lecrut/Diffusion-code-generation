import heapq

class GridPathfinder:
    def __init__(self, grid, diagonal_cost=1.414, cardinal_cost=1.0):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.diagonal_cost = diagonal_cost
        self.cardinal_cost = cardinal_cost
        self.visited = set()

    def heuristic(self, pos_a, pos_b):
        dx = abs(pos_a[0] - pos_b[0])
        dy = abs(pos_a[1] - pos_b[1])
        min_cost = min(dx, dy)
        max_cost = max(dx, dy)
        return min_cost * self.diagonal_cost + (max_cost - min_cost) * self.cardinal_cost

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = [
            ((x - 1, y), self.cardinal_cost),
            ((x + 1, y), self.cardinal_cost),
            ((x, y - 1), self.cardinal_cost),
            ((x, y + 1), self.cardinal_cost),
            ((x - 1, y - 1), self.diagonal_cost),
            ((x + 1, y + 1), self.diagonal_cost),
            ((x - 1, y + 1), self.diagonal_cost),
            ((x + 1, y - 1), self.diagonal_cost),
        ]
        valid_neighbors = []
        for (nx, ny), cost in neighbors:
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 0:
                valid_neighbors.append(((nx, ny), cost))
        return valid_neighbors

    def find_path(self, start, end):
        if self.grid[start[0]][start[1]] != 0 or self.grid[end[0]][end[1]] != 0:
            return None
        if start == end:
            return [start]
        
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}
        
        while open_set:
            current_f, current = heapq.heappop(open_set)
            
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(current)
                return path[::-1]
            
            if current in self.visited:
                continue
            self.visited.add(current)
            
            for neighbor, move_cost in self.get_neighbors(current):
                if neighbor in self.visited:
                    continue
                
                tentative_g = g_score[current] + move_cost
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor, end)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
        
        return None

def run():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    pathfinder = GridPathfinder(grid)
    start = (0, 0)
    end = (4, 4)
    path = pathfinder.find_path(start, end)
    print(path)

if __name__ == '__main__':
    run()