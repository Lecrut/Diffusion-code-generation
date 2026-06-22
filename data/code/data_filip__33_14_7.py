import heapq

class GridPathfinder:
    def __init__(self, grid, start, goal, diagonal_cost=1.41421356237):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.goal = goal
        self.diagonal_cost = diagonal_cost
        self.neighbors = self._get_neighbors()

    def _is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] != 0

    def _get_neighbors(self):
        return [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

    def _get_cost(self, dr, dc):
        if (dr != 0 and dc != 0):
            return self.diagonal_cost
        return 1.0

    def _heuristic(self, node):
        r, c = node
        gr, gc = self.goal
        return abs(r - gr) + abs(c - gc)

    def find_path(self):
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        g_score = {self.start: 0}
        f_score = {self.start: self._heuristic(self.start)}
        came_from = {}
        closed_set = set()

        while open_set:
            _, current = heapq.heappop(open_set)
            if current == self.goal:
                return self._reconstruct_path(came_from, current)
            if current in closed_set:
                continue
            closed_set.add(current)
            cr, cc = current
            for dr, dc in self.neighbors:
                nr, nc = cr + dr, cc + dc
                if not self._is_valid(nr, nc):
                    continue
                if (nr, nc) in closed_set:
                    continue
                if dr != 0 and dc != 0:
                    if not self._is_valid(cr, cc + dc) or not self._is_valid(cr + dr, cc):
                        continue
                tentative_g = g_score[current] + self._get_cost(dr, dc)
                neighbor = (nr, nc)
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self._heuristic(neighbor)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
        return None

    def _reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

if __name__ == '__main__':
    grid_data = [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    start_node = (0, 0)
    goal_node = (4, 4)
    pathfinder = GridPathfinder(grid_data, start_node, goal_node)
    result_path = pathfinder.find_path()
    print(result_path)