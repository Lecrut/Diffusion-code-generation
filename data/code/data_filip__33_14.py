import heapq

class GridPathfinder:
    def __init__(self, grid, diagonal_allowed=True):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.diagonal_allowed = diagonal_allowed

    def _is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def _get_neighbors(self, r, c, visited):
        neighbors = []
        moves = [
            (0, 1), (1, 0), (0, -1), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if self._is_valid(nr, nc):
                if self.diagonal_allowed or (dr == 0 or dc == 0):
                    cost = self.grid[nr][nc]
                    if (nr, nc) not in visited or cost < visited[(nr, nc)][1]:
                        neighbors.append(((nr, nc), cost, (dr, dc)))
        return neighbors

    def find_path(self, start, end):
        if not self._is_valid(start[0], start[1]) or not self._is_valid(end[0], end[1]):
            return None
        if self.grid[start[0]][start[1]] == 0:
            return None
        if self.grid[end[0]][end[1]] == 0:
            return None
        
        pq = [(self.grid[start[0]][start[1]], start, [])]
        visited = {start: (0, self.grid[start[0]][start[1]])}
        best_cost = {}
        
        while pq:
            current_cost, current_node, path = heapq.heappop(pq)
            
            if current_node == end:
                return path + [current_node]
            
            if current_node in best_cost and current_cost > best_cost[current_node]:
                continue
            best_cost[current_node] = current_cost
            
            r, c = current_node
            for (neighbor, cost, _) in self._get_neighbors(r, c, {}):
                new_cost = current_cost + cost
                if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                    best_cost[neighbor] = new_cost
                    new_path = path + [current_node]
                    heapq.heappush(pq, (new_cost, neighbor, new_path))
        
        return None

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 5, 2],
        [1, 1, 2, 4],
        [4, 1, 1, 1],
        [2, 4, 1, 1]
    ]
    start_pos = (0, 0)
    end_pos = (3, 3)
    finder = GridPathfinder(sample_grid, diagonal_allowed=True)
    result_path = finder.find_path(start_pos, end_pos)
    print(result_path)