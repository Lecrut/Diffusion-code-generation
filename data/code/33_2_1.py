import heapq

class GridPathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_path(self, start, goal):
        if self.grid[start[0]][start[1]] != 0 or self.grid[goal[0]][goal[1]] != 0:
            return None
        if start == goal:
            return [start]
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        closed_set = set()
        while open_set:
            current_priority, current = heapq.heappop(open_set)
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path
            if current in closed_set:
                continue
            closed_set.add(current)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                neighbor_row = current[0] + dr
                neighbor_col = current[1] + dc
                neighbor = (neighbor_row, neighbor_col)
                if not (0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols):
                    continue
                if self.grid[neighbor[0]][neighbor[1]] != 0:
                    continue
                if neighbor in closed_set:
                    continue
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
        return None

    def print_grid_with_path(self, path):
        if path is None:
            print("No path found")
            return
        display_grid = [row[:] for row in self.grid]
        for r, c in path:
            if display_grid[r][c] == 0:
                display_grid[r][c] = 2
        for row in display_grid:
            print(''.join(str(cell) if cell != 2 else 'X' for cell in row))

def main():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    pathfinder = GridPathfinder(grid)
    start = (0, 0)
    goal = (4, 4)
    path = pathfinder.find_path(start, goal)
    print(path)
    pathfinder.print_grid_with_path(path)

if __name__ == '__main__':
    main()