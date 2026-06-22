import heapq

class AStarPathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, pos):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            r, c = pos[0] + dr, pos[1] + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.grid[r][c] != 1:
                    neighbors.append((r, c))
        return neighbors

    def find_path(self, start, goal):
        if self.grid[start[0]][start[1]] == 1 or self.grid[goal[0]][goal[1]] == 1:
            return None

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)
                    if neighbor not in [item[1] for item in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    else:
                        for i, (_, node) in enumerate(open_set):
                            if node == neighbor:
                                open_set[i] = (f_score[neighbor], neighbor)
                                heapq.heapify(open_set)
                                break
        return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    pathfinder = AStarPathfinder(sample_grid)
    start_node = (0, 0)
    end_node = (4, 4)
    result_path = pathfinder.find_path(start_node, end_node)
    print(result_path)

    sample_grid_blocked = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    pathfinder_blocked = AStarPathfinder(sample_grid_blocked)
    result_blocked = pathfinder_blocked.find_path((0, 0), (2, 2))
    print(result_blocked)

    sample_grid_single = [
        [0]
    ]
    pathfinder_single = AStarPathfinder(sample_grid_single)
    result_single = pathfinder_single.find_path((0, 0), (0, 0))
    print(result_single)