import heapq

class GridPathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def _is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0

    def _heuristic(self, r, c, target_r, target_c):
        return abs(r - target_r) + abs(c - target_c)

    def find_path(self, start, end):
        start_r, start_c = start
        end_r, end_c = end

        if not self._is_valid(start_r, start_c) or not self._is_valid(end_r, end_c):
            return None, float('inf')

        open_set = []
        heapq.heappush(open_set, (0, 0, start_r, start_c))
        came_from = {}
        g_score = {(start_r, start_c): 0}
        f_score = {(start_r, start_c): self._heuristic(start_r, start_c, end_r, end_c)}
        visited = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while open_set:
            _, _, current_r, current_c = heapq.heappop(open_set)

            if (current_r, current_c) in visited:
                continue

            visited.add((current_r, current_c))

            if current_r == end_r and current_c == end_c:
                path = []
                curr = (current_r, current_c)
                while curr in came_from:
                    path.append(curr)
                    curr = came_from[curr]
                path.append(start)
                path.reverse()
                return path, g_score[(end_r, end_c)]

            for dr, dc in directions:
                neighbor_r, neighbor_c = current_r + dr, current_c + dc
                if not self._is_valid(neighbor_r, neighbor_c):
                    continue

                if (neighbor_r, neighbor_c) in visited:
                    continue

                tentative_g = g_score[(current_r, current_c)] + 1

                if tentative_g < g_score.get((neighbor_r, neighbor_c), float('inf')):
                    came_from[(neighbor_r, neighbor_c)] = (current_r, current_c)
                    g_score[(neighbor_r, neighbor_c)] = tentative_g
                    f = tentative_g + self._heuristic(neighbor_r, neighbor_c, end_r, end_c)
                    f_score[(neighbor_r, neighbor_c)] = f
                    heapq.heappush(open_set, (f, tentative_g, neighbor_r, neighbor_c))

        return None, float('inf')

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    pathfinder = GridPathfinder(grid)
    start_point = (0, 0)
    end_point = (4, 4)
    path, cost = pathfinder.find_path(start_point, end_point)
    print(path)
    print(cost)