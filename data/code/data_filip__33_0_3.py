from collections import deque
from typing import List, Tuple, Optional

def find_shortest_path(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None

    visited = set()
    visited.add(start)
    queue = deque([(start, [start])])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        (current_row, current_col), path = queue.popleft()

        if (current_row, current_col) == end:
            return path

        for dr, dc in directions:
            next_row, next_col = current_row + dr, current_col + dc

            if 0 <= next_row < rows and 0 <= next_col < cols:
                if grid[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    new_path = path + [(next_row, next_col)]
                    queue.append(((next_row, next_col), new_path))

    return None

if __name__ == '__main__':
    grid_sample = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    
    start_pos = (0, 0)
    end_pos = (4, 4)

    result_path = find_shortest_path(grid_sample, start_pos, end_pos)
    
    print(result_path)