import heapq
import math

class PathFinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def heuristic(self, n1, n2):
        x1, y1 = n1
        x2, y2 = n2
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return dx + dy + (math.sqrt(2) - 2) * min(dx, dy)

    def get_neighbors(self, pos):
        x, y = pos
        moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        neighbors = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.cols and 0 <= ny < self.rows:
                if self.grid[ny][nx] == 0:
                    weight = math.sqrt(2) if dx != 0 and dy != 0 else 1
                    neighbors.append(((nx, ny), weight))
        return neighbors

    def find_path(self, start, end):
        if self.grid[start[1]][start[0]] == 1 or self.grid[end[1]][end[0]] == 1:
            return None, float('inf')
        
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
                path.append(start)
                path.reverse()
                return path, g_score[end]
            
            del f_score[current]
            
            for neighbor, move_cost in self.get_neighbors(current):
                tentative_g = g_score[current] + move_cost
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor, end)
                    
                    if neighbor not in f_score:
                        heapq.heappush(open_set, (f, neighbor))
                        f_score[neighbor] = f
                    else:
                        f_score[neighbor] = f
                        heapq.heappush(open_set, (f, neighbor))
        
        return None, float('inf')

if __name__ == '__main__':
    grid_map = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    
    finder = PathFinder(grid_map)
    path, cost = finder.find_path(start_node, end_node)
    
    print(path)
    print(cost)