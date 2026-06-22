import heapq
from typing import List, Tuple, Optional

class AStarPathfinder:
    def __init__(self, grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end

    def _heuristic(self, current: Tuple[int, int]) -> int:
        return abs(current[0] - self.end[0]) + abs(current[1] - self.end[1])

    def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = pos
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for dr, dc in moves:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 0:
                neighbors.append((nr, nc))
        return neighbors

    def find_path(self) -> Optional[List[Tuple[int, int]]]:
        open_set = [(0, self.start)]
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self._heuristic(self.start)}
        closed_set = set()

        while open_set:
            _, current = heapq.heappop(open_set)

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
                
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self._heuristic(neighbor)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    pathfinder = AStarPathfinder(grid, (0, 0), (4, 4))
    result = pathfinder.find_path()
    print(result)