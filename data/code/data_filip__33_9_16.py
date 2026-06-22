import heapq

class AStarSolver:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def get_neighbors(self, node):
        r, c = node
        candidates = [
            (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1),
            (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)
        ]
        neighbors = []
        for nr, nc in candidates:
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 0:
                neighbors.append((nr, nc))
        return neighbors

    def heuristic(self, node, goal):
        r1, c1 = node
        r2, c2 = goal
        return max(abs(r1 - r2), abs(c1 - c2))

    def solve(self, start, goal):
        if self.grid[start[0]][start[1]] != 0 or self.grid[goal[0]][goal[1]] != 0:
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
                path.reverse()
                return path

            for neighbor in self.get_neighbors(current):
                r1, c1 = current
                r2, c2 = neighbor
                move_cost = 1.414 if (r1 != r2 and c1 != c2) else 1.0
                tentative_g = g_score[current] + move_cost

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    goal_node = (4, 4)
    solver = AStarSolver(sample_grid)
    result_path = solver.solve(start_node, goal_node)
    print(result_path)