import heapq

class GridPathfinder:
    def __init__(self, grid, cost_map=None):
        rows = len(grid)
        if rows == 0:
            raise ValueError("Grid cannot be empty")
        cols = len(grid[0])
        if cols == 0:
            raise ValueError("Grid columns cannot be empty")
        
        self.grid = grid
        self.rows = rows
        self.cols = cols
        self.cost_map = cost_map if cost_map is not None else {}

    def is_valid(self, r, c):
        if r < 0 or r >= self.rows:
            return False
        if c < 0 or c >= self.cols:
            return False
        if self.grid[r][c] == 0:
            return False
        return True

    def get_cost(self, r, c):
        key = (r, c)
        if key in self.cost_map:
            return self.cost_map[key]
        return 1.0

    def find_path(self, start, end):
        if not self.is_valid(start[0], start[1]) or not self.is_valid(end[0], end[1]):
            return []

        open_set = []
        heapq.heappush(open_set, (0.0, start))
        came_from = {}
        g_score = {start: 0.0}
        f_score = {start: self._heuristic(start, end)}
        closed_set = set()

        while open_set:
            current_f, current = heapq.heappop(open_set)

            if current == end:
                return self._reconstruct_path(came_from, current)

            if current in closed_set:
                continue
            closed_set.add(current)

            neighbors = self._get_neighbors(current)

            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current] + self._get_step_cost(current, neighbor)

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f = tentative_g_score + self._heuristic(neighbor, end)
                    f_score[neighbor] = f
                    if neighbor not in [n[1] for n in open_set]:
                        heapq.heappush(open_set, (f, neighbor))
                    else:
                        for i, (old_f, old_n) in enumerate(open_set):
                            if old_n == neighbor:
                                open_set[i] = (f, neighbor)
                                heapq.heapify(open_set)
                                break

        return []

    def _heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _get_step_cost(self, a, b):
        dr = abs(a[0] - b[0])
        dc = abs(a[1] - b[1])
        if dr == 1 and dc == 1:
            return 1.41421356
        if dr == 1 or dc == 1:
            return 1.0
        return 0.0

    def _get_neighbors(self, node):
        r, c = node
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        result = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.is_valid(nr, nc):
                result.append((nr, nc))
        return result

    def _reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]

if __name__ == '__main__':
    grid_map = [
        [1, 1, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1]
    ]
    
    pathfinder = GridPathfinder(grid_map)
    start_node = (0, 0)
    end_node = (4, 4)
    
    path = pathfinder.find_path(start_node, end_node)
    print(path)