import heapq
from typing import List, Tuple, Optional, Dict

class GridPathfinder:
    def __init__(self, grid: List[List[float]], start: Tuple[int, int], goal: Tuple[int, int]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.goal = goal
        self.diagonal_moves = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

    def is_valid(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def get_heuristic(self, r: int, c: int) -> float:
        dr = abs(r - self.goal[0])
        dc = abs(c - self.goal[1])
        return 14 * min(dr, dc) + 10 * (dr + dc - 2 * min(dr, dc))

    def find_path(self) -> Optional[List[Tuple[int, int]]]:
        if not self.is_valid(self.start[0], self.start[1]) or not self.is_valid(self.goal[0], self.goal[1]):
            return None
        if self.grid[self.start[0]][self.start[1]] < 0 or self.grid[self.goal[0]][self.goal[1]] < 0:
            return None

        open_heap: List[Tuple[float, int, int, int, int]] = []
        heapq.heappush(open_heap, (0, 0, self.start[0], self.start[1], 0))
        came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
        g_score: Dict[Tuple[int, int], float] = {self.start: 0}
        visited: set = set()

        while open_heap:
            _, _, curr_r, curr_c, _ = heapq.heappop(open_heap)
            current = (curr_r, curr_c)

            if current in visited:
                continue
            visited.add(current)

            if current == self.goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                return path

            current_g = g_score.get(current, float('inf'))

            for dr, dc in self.diagonal_moves:
                nr, nc = curr_r + dr, curr_c + dc
                neighbor = (nr, nc)

                if not self.is_valid(nr, nc):
                    continue
                if self.grid[nr][nc] < 0:
                    continue

                move_cost = 10 if abs(dr) + abs(dc) == 1 else 14
                total_cost = current_g + move_cost + self.grid[nr][nc]

                if neighbor not in g_score or total_cost < g_score[neighbor]:
                    g_score[neighbor] = total_cost
                    f_score = total_cost + self.get_heuristic(nr, nc)
                    heapq.heappush(open_heap, (f_score, id(neighbor), nr, nc, total_cost))
                    came_from[neighbor] = current

        return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 5, 5, 5, 0],
        [0, 0, 0, 5, 0],
        [0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    goal_point = (4, 4)
    finder = GridPathfinder(sample_grid, start_point, goal_point)
    result_path = finder.find_path()
    print(result_path)