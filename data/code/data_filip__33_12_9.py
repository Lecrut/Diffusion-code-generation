import heapq

class WeightedGridSolver:
    INF = float('inf')

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def _get_neighbors(self, r, c):
        neighbors = []
        current_weight = self.grid[r][c]
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if self._is_valid(nr, nc):
                neighbor_weight = self.grid[nr][nc]
                neighbors.append((nr, nc, neighbor_weight))
        return neighbors

    def solve(self, start, end):
        if self.rows == 0 or self.cols == 0:
            raise ValueError("Grid is empty")
        sr, sc = start
        er, ec = end
        if not self._is_valid(sr, sc):
            raise ValueError("Start coordinates out of bounds")
        if not self._is_valid(er, ec):
            raise ValueError("End coordinates out of bounds")
        if self.grid[sr][sc] == self.INF or self.grid[er][ec] == self.INF:
            raise ValueError("Start or end node is blocked")
        if start == end:
            return 0
        distances = {}
        for r in range(self.rows):
            for c in range(self.cols):
                distances[(r, c)] = self.INF
        distances[start] = 0
        pq = [(0, start[0], start[1])]
        while pq:
            d, r, c = heapq.heappop(pq)
            if r == er and c == ec:
                return d
            if d > distances[(r, c)]:
                continue
            for nr, nc, weight in self._get_neighbors(r, c):
                new_dist = d + weight
                if new_dist < distances[(nr, nc)]:
                    distances[(nr, nc)] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))
        return self.INF

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 2, 5],
        [4, 1, 3, 2],
        [float('inf'), 2, 1, 4],
        [3, 2, float('inf'), 1]
    ]
    start_point = (0, 0)
    end_point = (3, 3)
    solver = WeightedGridSolver(sample_grid)
    result = solver.solve(start_point, end_point)
    print(result)