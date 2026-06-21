import heapq
from typing import List, Tuple, Optional, Set

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class GridPathfinder:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def is_valid(self, point: Point) -> bool:
        return 0 <= point.x < self.rows and 0 <= point.y < self.cols and self.grid[point.x][point.y] == 0

    def get_neighbors(self, point: Point) -> List[Point]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            new_x = point.x + dx
            new_y = point.y + dy
            candidate = Point(new_x, new_y)
            if self.is_valid(candidate):
                neighbors.append(candidate)
        return neighbors

    def heuristic(self, a: Point, b: Point) -> int:
        return abs(a.x - b.x) + abs(a.y - b.y)

    def find_path(self, start: Point, end: Point) -> Optional[List[Point]]:
        if not self.is_valid(start) or not self.is_valid(end):
            return None

        open_set = []
        heapq.heappush(open_set, (0, start))
        
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}
        
        open_set_hash = {start}
        
        while open_set:
            current_f, current = heapq.heappop(open_set)
            open_set_hash.remove(current)
            
            if current == end:
                return self.reconstruct_path(came_from, current)
            
            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, end)
                    
                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        open_set_hash.add(neighbor)
        
        return None

    def reconstruct_path(self, came_from: dict, current: Point) -> List[Point]:
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    
    pathfinder = GridPathfinder(sample_grid)
    start_point = Point(0, 0)
    end_point = Point(4, 4)
    
    result_path = pathfinder.find_path(start_point, end_point)
    
    if result_path is not None:
        path_coords = [(p.x, p.y) for p in result_path]
        print(path_coords)
    else:
        print(None)