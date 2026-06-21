import heapq

class GridPathfinder:
    def __init__(self, grid, diagonal=True):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.diagonal = diagonal
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if diagonal:
            self.directions.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])

    def _get_neighbors(self, r, c):
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != 0:
                yield nr, nc

    def _get_cost(self, r1, c1, r2, c2):
        dist_sq = (r1 - r2) ** 2 + (c1 - c2) ** 2
        if dist_sq == 2:
            return 1.41421356237
        return 1.0

    def find_path(self, start, end):
        if self.grid[start[0]][start[1]] == 0 or self.grid[end[0]][end[1]] == 0:
            return None
        if start == end:
            return [start]
        
        open_set = [(0.0, start)]
        came_from = {}
        g_score = {start: 0.0}
        closed_set = set()
        
        while open_set:
            current_cost, current = heapq.heappop(open_set)
            
            if current == end:
                path = []
                node = end
                while node in came_from:
                    path.append(node)
                    node = came_from[node]
                path.append(start)
                path.reverse()
                return path
            
            if current in closed_set:
                continue
            closed_set.add(current)
            
            r, c = current
            for nr, nc in self._get_neighbors(r, c):
                neighbor = (nr, nc)
                if neighbor in closed_set:
                    continue
                
                move_cost = self._get_cost(r, c, nr, nc)
                tentative_g = g_score[current] + move_cost
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self._heuristic(nr, nc, end)
                    heapq.heappush(open_set, (f_score, neighbor))
        
        return None

    def _heuristic(self, r1, c1, r2, c2):
        dr = abs(r1 - r2)
        dc = abs(c1 - c2)
        return dr + dc + (1.41421356237 - 2) * min(dr, dc)

if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    pf = GridPathfinder(grid, diagonal=True)
    path = pf.find_path((0, 0), (4, 4))
    print(path)