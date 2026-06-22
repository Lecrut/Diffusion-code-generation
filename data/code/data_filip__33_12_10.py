import heapq
import sys

class DijkstraGrid:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.rows = len(grid)
        if self.rows == 0:
            self.cols = 0
            return
        self.cols = len(grid[0])
        self.start = start
        self.end = end
        self._validate_bounds()

    def _validate_bounds(self):
        if self.rows == 0 or self.cols == 0:
            return
        if not (0 <= self.start[0] < self.rows and 0 <= self.start[1] < self.cols):
            raise ValueError("Start position out of bounds")
        if not (0 <= self.end[0] < self.rows and 0 <= self.end[1] < self.cols):
            raise ValueError("End position out of bounds")
        if self.grid[self.start[0]][self.start[1]] < 0 or self.grid[self.end[0]][self.end[1]] < 0:
            raise ValueError("Start or end position has invalid weight")

    def _is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] >= 0

    def get_neighbors(self, r, c):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self._is_valid(nr, nc):
                neighbors.append((nr, nc, self.grid[nr][nc]))
        return neighbors

    def compute_shortest_path(self):
        if self.rows == 0 or self.cols == 0:
            return None, float('inf')
        if self.start == self.end:
            return [self.start], 0
        
        distances = {}
        previous = {}
        pq = [(0, self.start)]
        distances[self.start] = 0
        visited = set()

        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            visited.add(current)

            if current == self.end:
                path = []
                node = self.end
                while node != self.start:
                    path.append(node)
                    node = previous[node]
                path.append(self.start)
                path.reverse()
                return path, current_dist

            for nr, nc, weight in self.get_neighbors(current[0], current[1]):
                neighbor = (nr, nc)
                new_dist = current_dist + weight
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return None, float('inf')

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 2, 4],
        [1, 1, 5, 2],
        [2, 1, 1, 1],
        [10, 1, 5, 1]
    ]
    start_node = (0, 0)
    end_node = (3, 3)
    
    solver = DijkstraGrid(sample_grid, start_node, end_node)
    path, cost = solver.compute_shortest_path()
    print(f"Shortest Path: {path}")
    print(f"Total Cost: {cost}")