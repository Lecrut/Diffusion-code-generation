import heapq
import math

class AStarGrid:

    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = set()
        for obs in obstacles:
            self.obstacles.add(tuple(obs))

    def heuristic(self, a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        diagonal_cost = math.sqrt(2)
        straight_cost = 1.0
        min_ab = min(dx, dy)
        max_ab = max(dx, dy)
        return min_ab * diagonal_cost + (max_ab - min_ab) * straight_cost

    def get_neighbors(self, current):
        x, y = current
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        neighbors = []
        for dx, dy in moves:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < self.width and 0 <= ny < self.height:
                if (nx, ny) not in self.obstacles:
                    if dx != 0 and dy != 0:
                        if (x + dx, y) in self.obstacles or (x, y + dy) in self.obstacles:
                            continue
                    cost = 1.0 if dx == 0 or dy == 0 else math.sqrt(2)
                    neighbors.append(((nx, ny), cost))
        return neighbors

    def find_path(self, start, end):
        if start in self.obstacles or end in self.obstacles:
            return []
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}
        closed_set = set()
        while open_set:
            _, current = heapq.heappop(open_set)
            if current in closed_set:
                continue
            closed_set.add(current)
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path
            for neighbor, move_cost in self.get_neighbors(current):
                if neighbor in closed_set:
                    continue
                tentative_g = g_score[current] + move_cost
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return []
if __name__ == '__main__':
    grid = AStarGrid(10, 10, [(3, 3), (3, 4), (3, 5), (4, 4)])
    start_point = (0, 0)
    end_point = (9, 9)
    path = grid.find_path(start_point, end_point)
    print(path)