import heapq

class GridPathfinder:
    def __init__(self, grid, start, goal, diagonal=False):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.diagonal = diagonal
        self.height = len(grid)
        self.width = len(grid[0]) if self.height > 0 else 0

    def get_neighbors(self, node):
        row, col = node
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if self.diagonal:
            directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.height and 0 <= nc < self.width:
                if self.grid[nr][nc] != 0:
                    if self.diagonal and abs(dr) == 1 and abs(dc) == 1:
                        if self.grid[row][col + dc] == 0 or self.grid[row + dr][col] == 0:
                            continue
                    cost = self.grid[nr][nc]
                    if abs(dr) == 1 and abs(dc) == 1:
                        cost = cost * 1.41421356237
                    neighbors.append(((nr, nc), cost))
        return neighbors

    def heuristic(self, node):
        r1, c1 = node
        r2, c2 = self.goal
        if self.diagonal:
            return max(abs(r1 - r2), abs(c1 - c2)) * self.grid[self.goal[0]][self.goal[1]]
        return abs(r1 - r2) + abs(c1 - c2) * self.grid[self.goal[0]][self.goal[1]]

    def find_path(self):
        if self.grid[self.start[0]][self.start[1]] == 0 or self.grid[self.goal[0]][self.goal[1]] == 0:
            return []
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start)}
        while open_set:
            current_f, current = heapq.heappop(open_set)
            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                return path[::-1]
            if current_f > f_score.get(current, float('inf')):
                continue
            for neighbor, move_cost in self.get_neighbors(current):
                tentative_g = g_score[current] + move_cost
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return []

if __name__ == '__main__':
    grid_map = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    start_node = (0, 0)
    goal_node = (4, 4)
    finder = GridPathfinder(grid_map, start_node, goal_node, diagonal=True)
    result_path = finder.find_path()
    print(result_path)