import heapq

class GridSolver:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0

    def solve(self):
        if not self.grid or not self.start or not self.end:
            return None
        
        sr, sc = self.start
        er, ec = self.end
        
        if not self.is_valid(sr, sc) or not self.is_valid(er, ec):
            return None

        distances = {}
        for r in range(self.rows):
            for c in range(self.cols):
                distances[(r, c)] = float('inf')
        
        distances[self.start] = 0
        pq = [(0, self.start)]
        previous = {}

        while pq:
            current_dist, current_pos = heapq.heappop(pq)
            
            if current_pos == self.end:
                path = []
                curr = self.end
                while curr != self.start:
                    path.append(curr)
                    curr = previous[curr]
                path.append(self.start)
                path.reverse()
                return path

            if current_dist > distances[current_pos]:
                continue

            r, c = current_pos
            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                if self.is_valid(nr, nc):
                    new_dist = current_dist + 1
                    if new_dist < distances.get((nr, nc), float('inf')):
                        distances[(nr, nc)] = new_dist
                        previous[(nr, nc)] = current_pos
                        heapq.heappush(pq, (new_dist, (nr, nc)))
        
        return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    solver = GridSolver(sample_grid, start_node, end_node)
    result_path = solver.solve()
    print(result_path)