import heapq
import math

class AStarGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.diagonal_costs = math.sqrt(2)

    def set_obstacle(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 1

    def is_valid(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        if self.grid[y][x] == 1:
            return False
        return True

    def get_neighbors(self, x, y):
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                cost = self.diagonal_costs if dx != 0 and dy != 0 else 1.0
                neighbors.append((nx, ny, cost))
        return neighbors

    def heuristic(self, a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        return max(dx, dy) * self.diagonal_costs

    def find_path(self, start, end):
        if not self.is_valid(start[0], start[1]) or not self.is_valid(end[0], end[1]):
            return None

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}
        open_set_hash = {start}

        while open_set:
            current = heapq.heappop(open_set)[1]
            open_set_hash.discard(current)

            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path

            for nx, ny, cost in self.get_neighbors(current[0], current[1]):
                neighbor = (nx, ny)
                tentative_g = g_score[current] + cost
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, end)
                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        open_set_hash.add(neighbor)
        return None

if __name__ == '__main__':
    grid = AStarGrid(10, 10)
    grid.set_obstacle(2, 2)
    grid.set_obstacle(3, 2)
    grid.set_obstacle(4, 2)
    grid.set_obstacle(5, 3)
    grid.set_obstacle(5, 4)
    grid.set_obstacle(5, 5)
    grid.set_obstacle(6, 6)
    grid.set_obstacle(7, 6)
    start_node = (0, 0)
    end_node = (8, 8)
    path = grid.find_path(start_node, end_node)
    print(path)