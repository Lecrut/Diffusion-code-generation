import heapq
import math

class GridPathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def get_neighbors(self, pos):
        r, c = pos
        neighbors = []
        moves = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] == 0:
                    is_diagonal = dr != 0 and dc != 0
                    if is_diagonal:
                        if self.grid[r][c + dc] != 0 or self.grid[r + dr][c] != 0:
                            continue
                    neighbors.append((nr, nc))
        return neighbors

    def heuristic(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def get_move_cost(self, current, neighbor):
        dr = abs(current[0] - neighbor[0])
        dc = abs(current[1] - neighbor[1])
        if dr == 1 and dc == 1:
            return math.sqrt(2)
        return 1

    def find_path(self, start, goal):
        if not self.grid or self.grid[start[0]][start[1]] != 0 or self.grid[goal[0]][goal[1]] != 0:
            return None

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + self.get_move_cost(current, neighbor)
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor, goal)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))

        return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)
    pathfinder = GridPathfinder(grid)
    result = pathfinder.find_path(start, goal)
    print(result)