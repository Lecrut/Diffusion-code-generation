import heapq
from typing import List, Tuple, Optional, Set, Dict

class GridPathfinder:
    def __init__(self, grid: List[List[int]], diagonal_cost: float = 1.414):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.diagonal_cost = diagonal_cost
        self._obstacles = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1:
                    self._obstacles.add((r, c))

    def find_shortest_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[List[Tuple[int, int]], float]:
        if start in self._obstacles or end in self._obstacles:
            return [], float('inf')
        if not (0 <= start[0] < self.rows and 0 <= start[1] < self.cols):
            return [], float('inf')
        if not (0 <= end[0] < self.rows and 0 <= end[1] < self.cols):
            return [], float('inf')

        dist = {}
        prev = {}
        open_set = [(0, start)]
        dist[start] = 0

        while open_set:
            current_dist, current_node = heapq.heappop(open_set)

            if current_node == end:
                path = []
                node = current_node
                while node is not None:
                    path.append(node)
                    node = prev.get(node, None)
                path.reverse()
                return path, current_dist

            if current_dist > dist.get(current_node, float('inf')):
                continue

            r, c = current_node
            neighbors = self._get_neighbors(r, c)

            for nr, nc, cost in neighbors:
                neighbor = (nr, nc)
                tentative_dist = current_dist + cost

                if tentative_dist < dist.get(neighbor, float('inf')):
                    dist[neighbor] = tentative_dist
                    prev[neighbor] = current_node
                    heapq.heappush(open_set, (tentative_dist, neighbor))

        return [], float('inf')

    def _get_neighbors(self, r: int, c: int) -> List[Tuple[int, int, float]]:
        neighbors = []
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self._obstacles:
                if i % 2 == 0:
                    cost = self.diagonal_cost
                else:
                    cost = 1.0
                neighbors.append((nr, nc, cost))

        return neighbors

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_pos = (0, 0)
    end_pos = (4, 4)

    pathfinder = GridPathfinder(sample_grid)
    path, cost = pathfinder.find_shortest_path(start_pos, end_pos)

    print(path)
    print(cost)