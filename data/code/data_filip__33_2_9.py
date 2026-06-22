import heapq

class GridPathfinder:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.goal = goal

    def heuristic(self, node):
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def is_valid(self, node):
        return (0 <= node[0] < self.rows and
                0 <= node[1] < self.cols and
                self.grid[node[0]][node[1]] == 0)

    def get_neighbors(self, node):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            new_row, new_col = node[0] + dr, node[1] + dc
            if self.is_valid((new_row, new_col)):
                neighbors.append((new_row, new_col))
        return neighbors

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        if path[0] != self.start:
            return None
        return path

    def find_path(self):
        if not self.is_valid(self.start) or not self.is_valid(self.goal):
            return None

        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start)}
        closed_set = set()

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.goal:
                return self.reconstruct_path(came_from, current)

            if current in closed_set:
                continue
            closed_set.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in closed_set:
                    continue
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))

        return None

if __name__ == '__main__':
    grid1 = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start1 = (0, 0)
    goal1 = (4, 4)
    pf1 = GridPathfinder(grid1, start1, goal1)
    path1 = pf1.find_path()
    print(path1)

    grid2 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start2 = (0, 0)
    goal2 = (2, 2)
    pf2 = GridPathfinder(grid2, start2, goal2)
    path2 = pf2.find_path()
    print(path2)

    grid3 = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    start3 = (0, 0)
    goal3 = (2, 2)
    pf3 = GridPathfinder(grid3, start3, goal3)
    path3 = pf3.find_path()
    print(path3)