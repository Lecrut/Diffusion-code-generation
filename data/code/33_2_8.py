import heapq

class GridPathfinder:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _heuristic(self, pos):
        return abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])

    def _is_valid(self, pos):
        r, c = pos
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r][c] == 0
        return False

    def find_path(self):
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self._heuristic(self.start)}
        in_open_set = {self.start}

        while open_set:
            _, current = heapq.heappop(open_set)
            in_open_set.discard(current)

            if current == self.end:
                return self._reconstruct_path(came_from, current)

            cr, cc = current
            for dr, dc in self.directions:
                neighbor = (cr + dr, cc + dc)
                if not self._is_valid(neighbor):
                    continue

                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self._heuristic(neighbor)
                    f_score[neighbor] = f
                    if neighbor not in in_open_set:
                        heapq.heappush(open_set, (f, neighbor))
                        in_open_set.add(neighbor)
        return []

    def _reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    pathfinder = GridPathfinder(grid, start, end)
    result = pathfinder.find_path()
    print(result)