import heapq
from typing import List, Tuple, Optional

def shortest_path_binary_grid(grid: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return None
    start = (0, 0)
    target = (rows - 1, cols - 1)
    pq = [(0, 0, 0)]
    visited = set()
    visited.add((0, 0))
    parent = {start: None}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while pq:
        cost, x, y = heapq.heappop(pq)
        if (x, y) == target:
            path = []
            current = target
            while current is not None:
                path.append(current)
                current = parent.get(current)
            return list(reversed(path))
        for dx, dy in directions:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) not in visited and grid[nx][ny] == 0:
                    visited.add((nx, ny))
                    parent[nx, ny] = (x, y)
                    heapq.heappush(pq, (cost + 1, nx, ny))
    return None
if __name__ == '__main__':
    sample_grid = [[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]]
    result = shortest_path_binary_grid(sample_grid)
    print(result)