import heapq

class GridPathfinder:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.costs = {
            (0, 1): 1.0,
            (0, -1): 1.0,
            (1, 0): 1.0,
            (-1, 0): 1.0,
            (1, 1): 1.414,
            (1, -1): 1.414,
            (-1, 1): 1.414,
            (-1, -1): 1.414,
        }

    def heuristic(self, node):
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def is_valid(self, node):
        return 0 <= node[0] < self.rows and 0 <= node[1] < self.cols and self.grid[node[0]][node[1]] != 1

    def get_neighbors(self, node):
        neighbors = []
        for dy, dx in self.costs:
            neighbor = (node[0] + dy, node[1] + dx)
            if self.is_valid(neighbor):
                if abs(dy) + abs(dx) == 2 and (self.grid[node[0] + dy][node[1]] == 1 or self.grid[node[0]][node[1] + dx] == 1):
                    continue
                neighbors.append((neighbor, self.costs[(dy, dx)]))
        return neighbors

    def find_path(self):
        open_set = [(0, self.heuristic(self.start), self.start)]
        g_score = {self.start: 0}
        came_from = {}

        while open_set:
            _, _, current = heapq.heappop(open_set)

            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                return path[::-1]

            for neighbor, cost in self.get_neighbors(current):
                tentative_g_score = g_score[current] + cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor)
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (f_score, f_score, neighbor))

        return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start = (0, 0)
    goal = (4, 4)

    pathfinder = GridPathfinder(grid, start, goal)
    path = pathfinder.find_path()
    print(path)