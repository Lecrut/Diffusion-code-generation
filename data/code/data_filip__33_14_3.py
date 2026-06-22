import heapq
from typing import List, Tuple, Dict, Optional, Set

class GridPathfinder:
    def __init__(self, grid: List[List[float]], start: Tuple[int, int], end: Tuple[int, int]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end
        self._costs = {}
        self._previous = {}
        self._open_set = []
        self._closed_set = set()

    def heuristic(self, node: Tuple[int, int]) -> float:
        x1, y1 = node
        x2, y2 = self.end
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        min_dist = min(dx, dy)
        diff = abs(dx - dy)
        return min_dist * 1.414 + diff

    def neighbors(self, node: Tuple[int, int]) -> List[Tuple[Tuple[int, int], float]]:
        x, y = node
        directions = [
            (0, 1, 1.0), (0, -1, 1.0), (1, 0, 1.0), (-1, 0, 1.0),
            (1, 1, 1.414), (1, -1, 1.414), (-1, 1, 1.414), (-1, -1, 1.414)
        ]
        result = []
        for dx, dy, cost in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] != 0:
                result.append(((nx, ny), cost))
        return result

    def find_path(self) -> List[Tuple[int, int]]:
        self._costs = {self.start: 0}
        self._previous = {self.start: None}
        self._open_set = [(0, self.start)]
        self._closed_set = set()

        while self._open_set:
            current_cost, current = heapq.heappop(self._open_set)
            
            if current in self._closed_set:
                continue
                
            if current == self.end:
                return self._reconstruct_path(current)
            
            self._closed_set.add(current)
            
            for neighbor, move_cost in self.neighbors(current):
                if neighbor in self._closed_set:
                    continue
                
                new_cost = current_cost + move_cost * self.grid[neighbor][neighbor]
                
                if neighbor not in self._costs or new_cost < self._costs[neighbor]:
                    self._costs[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor)
                    self._previous[neighbor] = current
                    heapq.heappush(self._open_set, (priority, neighbor))
        
        return []

    def _reconstruct_path(self, current: Tuple[int, int]) -> List[Tuple[int, int]]:
        path = []
        while current is not None:
            path.append(current)
            current = self._previous.get(current)
        path.reverse()
        return path

if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    start = (0, 0)
    end = (4, 4)
    pathfinder = GridPathfinder(grid, start, end)
    path = pathfinder.find_path()
    print(path)