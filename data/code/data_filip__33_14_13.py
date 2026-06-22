import heapq
from collections import deque

class GridPathfinder:
    def __init__(self, grid, costs=None):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.costs = costs if costs is not None else {}

    def _get_neighbors(self, r, c):
        deltas = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        neighbors = []
        for dr, dc in deltas:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != 1:
                    neighbors.append((nr, nc))
        return neighbors

    def _get_move_cost(self, r, c, nr, nc):
        if (r, c) in self.costs and (nr, nc) in self.costs[(r, c)]:
            return self.costs[(r, c)][(nr, nc)]
        if (r, c) in self.costs:
            if (nr, nc) in self.costs[(r, c)]:
                return self.costs[(r, c)][(nr, nc)]
        if abs(nr - r) + abs(nc - c) == 1:
            return 10
        return 14

    def find_path(self, start, end):
        if not (0 <= start[0] < self.rows and 0 <= start[1] < self.cols):
            return None
        if not (0 <= end[0] < self.rows and 0 <= end[1] < self.cols):
            return None
        if self.grid[start[0]][start[1]] == 1 or self.grid[end[0]][end[1]] == 1:
            return None

        heap = [(0, start)]
        came_from = {start: None}
        cost_so_far = {start: 0}

        while heap:
            current_cost, current = heapq.heappop(heap)

            if current == end:
                path = []
                node = end
                while node is not None:
                    path.append(node)
                    node = came_from[node]
                return list(reversed(path))

            if current_cost > cost_so_far.get(current, float('inf')):
                continue

            for neighbor in self._get_neighbors(current[0], current[1]):
                new_cost = cost_so_far[current] + self._get_move_cost(current[0], current[1], neighbor[0], neighbor[1])
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self._heuristic(neighbor, end)
                    heapq.heappush(heap, (priority, neighbor))
                    came_from[neighbor] = current
        return None

    def _heuristic(self, node, end):
        r, c = node
        er, ec = end
        return 14 * min(abs(er - r), abs(ec - c)) + 10 * (abs(er - r) + abs(ec - c) - 2 * min(abs(er - r), abs(ec - c)))

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    sample_costs = {}
    finder = GridPathfinder(sample_grid, sample_costs)
    result = finder.find_path((0, 0), (4, 4))
    print(result)