import heapq

class AStarGridPathfinder:
    def __init__(self, grid_rows, grid_cols, start, goal, obstacles):
        self.rows = grid_rows
        self.cols = grid_cols
        self.start = start
        self.goal = goal
        self.obstacles = set(obstacles)
        self.directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        self.diag_cost = 1.41421356
        self.cardinal_cost = 1.0

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and (r, c) not in self.obstacles

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_path(self):
        if self.start in self.obstacles or self.goal in self.obstacles:
            return None
        
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}
        
        while open_set:
            current_f, current = heapq.heappop(open_set)
            
            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                path.reverse()
                return path
            
            for dr, dc in self.directions:
                neighbor = (current[0] + dr, current[1] + dc)
                
                if not self.is_valid(neighbor[0], neighbor[1]):
                    continue
                
                move_cost = self.diag_cost if dr != 0 and dc != 0 else self.cardinal_cost
                tentative_g = g_score[current] + move_cost
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor, self.goal)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
        
        return None

if __name__ == '__main__':
    grid_rows = 10
    grid_cols = 10
    start_pos = (0, 0)
    goal_pos = (5, 5)
    obstacle_list = [(1, 0), (1, 1), (2, 1), (3, 2), (3, 3), (4, 4), (5, 4)]
    
    pathfinder = AStarGridPathfinder(grid_rows, grid_cols, start_pos, goal_pos, obstacle_list)
    result_path = pathfinder.find_path()
    
    print(result_path)