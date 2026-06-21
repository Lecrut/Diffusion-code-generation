import heapq
from typing import List, Tuple, Optional, Dict, Set

class GridPathfinder:
    def __init__(self, grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int], allow_diagonal: bool = False):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.goal = goal
        self.allow_diagonal = allow_diagonal
        self.visited: Set[Tuple[int, int]] = set()
        self.parents: Dict[Tuple[int, int], Tuple[int, int]] = {}
        self.g_scores: Dict[Tuple[int, int], float] = {}
        self._validate_bounds()

    def _validate_bounds(self):
        if not (0 <= self.start[0] < self.rows and 0 <= self.start[1] < self.cols):
            raise ValueError("Start position out of bounds")
        if not (0 <= self.goal[0] < self.rows and 0 <= self.goal[1] < self.cols):
            raise ValueError("Goal position out of bounds")
        if self.grid[self.start[0]][self.start[1]] == 0:
            raise ValueError("Start position is an obstacle")
        if self.grid[self.goal[0]][self.goal[1]] == 0:
            raise ValueError("Goal position is an obstacle")

    def _get_neighbors(self, r: int, c: int) -> List[Tuple[int, int, float]]:
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if self.allow_diagonal:
            moves.extend([(-1, -1), (-1, 1), (1, -1), (1, 1)])
        neighbors = []
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != 0:
                    cost = self.grid[nr][nc] * (1.41421356 if self.allow_diagonal and dr != 0 and dc != 0 else 1.0)
                    neighbors.append((nr, nc, cost))
        return neighbors

    def find_optimal_path(self) -> Tuple[Optional[List[Tuple[int, int]]], float]:
        if self.start == self.goal:
            return [self.start], self.grid[self.start[0]][self.start[1]]
        open_set: List[Tuple[float, int, int]] = []
        heapq.heappush(open_set, (0.0, self.start[0], self.start[1]))
        self.g_scores[self.start] = self.grid[self.start[0]][self.start[1]]
        self.visited.clear()
        self.parents.clear()
        while open_set:
            current_f, r, c = heapq.heappop(open_set)
            if (r, c) in self.visited:
                continue
            self.visited.add((r, c))
            if (r, c) == self.goal:
                return self._reconstruct_path(), self.g_scores[self.goal]
            current_g = self.g_scores.get((r, c), float('inf'))
            for nr, nc, move_cost in self._get_neighbors(r, c):
                if (nr, nc) in self.visited:
                    continue
                tentative_g = current_g + move_cost
                if tentative_g < self.g_scores.get((nr, nc), float('inf')):
                    self.parents[(nr, nc)] = (r, c)
                    self.g_scores[(nr, nc)] = tentative_g
                    heuristic = self._calculate_heuristic(nr, nc)
                    f_score = tentative_g + heuristic
                    heapq.heappush(open_set, (f_score, nr, nc))
        return None, -1.0

    def _calculate_heuristic(self, r: int, c: int) -> float:
        dr = abs(r - self.goal[0])
        dc = abs(c - self.goal[1])
        if self.allow_diagonal:
            return (1.41421356 * min(dr, dc)) + (1.0 * abs(dr - dc))
        else:
            return float(dr + dc)

    def _reconstruct_path(self) -> List[Tuple[int, int]]:
        path: List[Tuple[int, int]] = []
        current = self.goal
        while current != self.start:
            path.append(current)
            current = self.parents[current]
        path.append(self.start)
        path.reverse()
        return path

if __name__ == '__main__':
    sample_grid = [
        [1, 2, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 2, 1, 2, 1],
        [1, 1, 0, 1, 1],
        [1, 2, 1, 1, 1]
    ]
    start_pos = (0, 0)
    goal_pos = (4, 4)
    pathfinder = GridPathfinder(sample_grid, start_pos, goal_pos, allow_diagonal=True)
    path, total_cost = pathfinder.find_optimal_path()
    print(f"Path: {path}")
    print(f"Total Cost: {total_cost}")