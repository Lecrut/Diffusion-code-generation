import heapq
from typing import List, Tuple, Optional

class ShortestPathFinder:
    def __init__(self, grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]):
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.visited = set()
        self.previous = {}

    def is_valid(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def get_neighbors(self, row: int, col: int) -> List[Tuple[int, int, int]]:
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if self.is_valid(nr, nc):
                neighbors.append((nr, nc, self.grid[nr][nc]))
        return neighbors

    def find_path(self) -> Optional[List[Tuple[int, int]]]:
        if not self.is_valid(*self.start) or not self.is_valid(*self.end):
            return None
        if self.grid[self.start[0]][self.start[1]] < 0 or self.grid[self.end[0]][self.end[1]] < 0:
            return None
        
        priority_queue = [(self.grid[self.start[0]][self.start[1]], self.start)]
        distances = {self.start: self.grid[self.start[0]][self.start[1]]}
        
        while priority_queue:
            current_dist, current_pos = heapq.heappop(priority_queue)
            
            if current_pos in self.visited:
                continue
            
            self.visited.add(current_pos)
            
            if current_pos == self.end:
                break
            
            if current_dist > distances.get(current_pos, float('inf')):
                continue
            
            for nr, nc, weight in self.get_neighbors(*current_pos):
                if (nr, nc) in self.visited:
                    continue
                
                new_dist = current_dist + weight
                
                if new_dist < distances.get((nr, nc), float('inf')):
                    distances[(nr, nc)] = new_dist
                    self.previous[(nr, nc)] = current_pos
                    heapq.heappush(priority_queue, (new_dist, (nr, nc)))
        
        if self.end not in self.previous and self.end != self.start:
            return None
        
        path = []
        current = self.end
        path.append(current)
        while current != self.start:
            if current not in self.previous:
                return None
            current = self.previous[current]
            path.append(current)
        
        return path[::-1]

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    sample_start = (0, 0)
    sample_end = (2, 2)
    
    finder = ShortestPathFinder(sample_grid, sample_start, sample_end)
    result_path = finder.find_path()
    print(result_path)