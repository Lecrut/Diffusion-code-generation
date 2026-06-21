import heapq

class AStarSearch:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def get_neighbors(self, pos):
        r, c = pos
        candidates = [
            (r - 1, c), (r + 1, c),
            (r, c - 1), (r, c + 1),
            (r - 1, c - 1), (r - 1, c + 1),
            (r + 1, c - 1), (r + 1, c + 1)
        ]
        valid = []
        for nr, nc in candidates:
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] == 0:
                    valid.append((nr, nc))
        return valid

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def search(self, start, goal):
        if self.grid[start[0]][start[1]] == 1 or self.grid[goal[0]][goal[1]] == 1:
            return None
        
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}
        open_set_hash = {start}

        while open_set:
            current = heapq.heappop(open_set)[1]
            open_set_hash.remove(current)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return list(reversed(path))

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor, goal)
                    f_score[neighbor] = f
                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f, neighbor))
                        open_set_hash.add(neighbor)
        return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    goal_node = (4, 4)
    searcher = AStarSearch(grid)
    result = searcher.search(start_node, goal_node)
    print(result)