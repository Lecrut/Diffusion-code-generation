import heapq
from typing import List, Tuple, Optional, Set

class AStarPathfinder:
    def __init__(self, grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end

    def _heuristic(self, current: Tuple[int, int]) -> int:
        return abs(current[0] - self.end[0]) + abs(current[1] - self.end[1])

    def _is_valid(self, position: Tuple[int, int]) -> bool:
        r, c = position
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r][c] == 0
        return False

    def find_path(self) -> Optional[List[Tuple[int, int]]]:
        if not self._is_valid(self.start) or not self._is_valid(self.end):
            return None
        
        open_set: List[Tuple[int, int, Tuple[int, int]]] = []
        heapq.heappush(open_set, (self._heuristic(self.start), 0, self.start))
        
        came_from: dict[Tuple[int, int], Optional[Tuple[int, int]]] = {}
        g_score: dict[Tuple[int, int], int] = {self.start: 0}
        open_set_hash: Set[Tuple[int, int]] = {self.start}
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while open_set:
            _, current_cost, current = heapq.heappop(open_set)
            
            if current not in open_set_hash:
                continue
            open_set_hash.remove(current)
            
            if current == self.end:
                return self._reconstruct_path(came_from, current)
            
            for dr, dc in directions:
                neighbor = (current[0] + dr, current[1] + dc)
                
                if not self._is_valid(neighbor):
                    continue
                
                tentative_g_score = current_cost + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self._heuristic(neighbor)
                    heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))
                    if neighbor not in open_set_hash:
                        open_set_hash.add(neighbor)
        
        return None

    def _reconstruct_path(self, came_from: dict[Tuple[int, int], Optional[Tuple[int, int]]], current: Tuple[int, int]) -> List[Tuple[int, int]]:
        path = [current]
        while current in came_from and came_from[current] is not None:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

if __name__ == '__main__':
    grid1 = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0]
    ]
    start1 = (0, 0)
    end1 = (3, 4)
    finder1 = AStarPathfinder(grid1, start1, end1)
    path1 = finder1.find_path()
    print(path1)

    grid2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    start2 = (0, 0)
    end2 = (2, 2)
    finder2 = AStarPathfinder(grid2, start2, end2)
    path2 = finder2.find_path()
    print(path2)

    grid3 = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    start3 = (0, 0)
    end3 = (2, 2)
    finder3 = AStarPathfinder(grid3, start3, end3)
    path3 = finder3.find_path()
    print(path3)

    grid4 = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 0]
    ]
    start4 = (0, 0)
    end4 = (2, 2)
    finder4 = AStarPathfinder(grid4, start4, end4)
    path4 = finder4.find_path()
    print(path4)