import heapq

class AStarSearch:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_shortest_path(self, start, goal):
        if not (0 <= start[0] < self.rows and 0 <= start[1] < self.cols) or self.grid[start[0]][start[1]] == 1:
            return None
        if not (0 <= goal[0] < self.rows and 0 <= goal[1] < self.cols) or self.grid[goal[0]][goal[1]] == 1:
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
            
            for dx, dy in self.directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < self.rows and 0 <= neighbor[1] < self.cols:
                    if self.grid[neighbor[0]][neighbor[1]] == 1:
                        continue
                    
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    search_engine = AStarSearch(sample_grid)
    result_path = search_engine.find_shortest_path(start_point, end_point)
    print(result_path)