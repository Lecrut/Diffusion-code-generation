import heapq
from typing import List, Tuple, Set, Optional

class GridPathfinder:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def _heuristic(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> int:
        r1, c1 = pos
        r2, c2 = goal
        return abs(r1 - r2) + abs(c1 - c2)

    def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        r, c = pos
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] == 0:
                    neighbors.append((nr, nc))
        return neighbors

    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        if not self.is_valid(start) or not self.is_valid(goal):
            return None
        if self.grid[start[0]][start[1]] == 1 or self.grid[goal[0]][goal[1]] == 1:
            return None

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self._heuristic(start, goal)}
        closed_set = set()

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

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
                    f = tentative_g + self._heuristic(neighbor, goal)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
        
        return None

    def is_valid(self, pos: Tuple[int, int]) -> bool:
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

def main():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    pathfinder = GridPathfinder(grid)
    start = (0, 0)
    goal = (4, 4)
    
    result = pathfinder.find_path(start, goal)
    print(result)

    grid2 = [
        [0, 0],
        [1, 0]
    ]
    pathfinder2 = GridPathfinder(grid2)
    start2 = (0, 0)
    goal2 = (1, 1)
    result2 = pathfinder2.find_path(start2, goal2)
    print(result2)

if __name__ == '__main__':
    main()