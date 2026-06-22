import heapq
from collections import namedtuple

State = namedtuple('State', ['g', 'h', 'pos', 'path'])

class AStarPathfinder:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end
        self.open_set = []
        self.closed_set = set()
        self.g_score = {}
        self.f_score = {}
        self.came_from = {}

    def heuristic(self, pos):
        return abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])

    def is_valid(self, pos):
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0

    def neighbors(self, pos):
        r, c = pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.is_valid((nr, nc)):
                result.append((nr, nc))
        return result

    def find_path(self):
        self.g_score[self.start] = 0
        self.f_score[self.start] = self.heuristic(self.start)
        heapq.heappush(self.open_set, (self.f_score[self.start], self.f_score[self.start], self.start))

        while self.open_set:
            _, _, current = heapq.heappop(self.open_set)

            if current == self.end:
                path = []
                while current in self.came_from:
                    path.append(current)
                    current = self.came_from[current]
                path.append(self.start)
                path.reverse()
                return path

            self.closed_set.add(current)

            for neighbor in self.neighbors(current):
                if neighbor in self.closed_set:
                    continue

                tentative_g = self.g_score[current] + 1

                if neighbor not in self.g_score or tentative_g < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g
                    h = self.heuristic(neighbor)
                    self.f_score[neighbor] = tentative_g + h
                    heapq.heappush(self.open_set, (self.f_score[neighbor], h, neighbor))

        return []

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)

    pathfinder = AStarPathfinder(grid, start, end)
    path = pathfinder.find_path()
    print(path)

    grid2 = [
        [0, 1],
        [0, 0]
    ]
    start2 = (0, 0)
    end2 = (1, 1)

    pathfinder2 = AStarPathfinder(grid2, start2, end2)
    path2 = pathfinder2.find_path()
    print(path2)

    grid3 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start3 = (0, 0)
    end3 = (2, 2)

    pathfinder3 = AStarPathfinder(grid3, start3, end3)
    path3 = pathfinder3.find_path()
    print(path3)