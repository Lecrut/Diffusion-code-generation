import heapq

class GridPathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = None
        self.end = None
        self.obstacles = set()
        self._parse_grid()

    def _parse_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                if cell == 'S':
                    self.start = (r, c)
                elif cell == 'E':
                    self.end = (r, c)
                elif cell == 'X':
                    self.obstacles.add((r, c))

    def _heuristic(self, node):
        dr = abs(node[0] - self.end[0])
        dc = abs(node[1] - self.end[1])
        return dr + dc

    def _get_neighbors(self, node):
        r, c = node
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.obstacles:
                neighbors.append((nr, nc))
        return neighbors

    def find_path(self):
        if not self.start or not self.end:
            return []

        open_set = []
        heapq.heappush(open_set, (0, 0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self._heuristic(self.start)}
        closed_set = set()

        while open_set:
            _, current_idx, current = heapq.heappop(open_set)

            if current == self.end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                path.reverse()
                return path

            if current in closed_set:
                continue
            closed_set.add(current)

            for neighbor in self._get_neighbors(current):
                if neighbor in closed_set:
                    continue

                tentative_g = g_score.get(current, float('inf')) + 1

                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self._heuristic(neighbor)
                    f_score[neighbor] = f
                    entry = (f, current_idx + 1, neighbor)
                    heapq.heappush(open_set, entry)

        return []

if __name__ == '__main__':
    grid1 = [
        ['S', '.', '.', '.', '.'],
        ['.', '.', 'X', 'X', '.'],
        ['.', '.', '.', 'X', '.'],
        ['.', '.', '.', '.', 'E']
    ]
    pf1 = GridPathfinder(grid1)
    path1 = pf1.find_path()
    print(path1)

    grid2 = [
        ['S', 'X', 'X'],
        ['.', '.', '.'],
        ['X', 'X', 'E']
    ]
    pf2 = GridPathfinder(grid2)
    path2 = pf2.find_path()
    print(path2)

    grid3 = [
        ['S', '.', '.'],
        ['.', 'X', '.'],
        ['.', '.', 'E']
    ]
    pf3 = GridPathfinder(grid3)
    path3 = pf3.find_path()
    print(path3)