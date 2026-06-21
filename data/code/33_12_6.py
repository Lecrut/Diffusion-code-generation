import heapq
from typing import List, Tuple, Optional, Dict, Set

def shortest_path_dijkstra(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[Tuple[List[Tuple[int, int]], int]]:
    if not grid or not grid[0]:
        return None

    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = start
    end_row, end_col = end

    if not (0 <= start_row < rows and 0 <= start_col < cols):
        return None
    if not (0 <= end_row < rows and 0 <= end_col < cols):
        return None
    if grid[start_row][start_col] == -1 or grid[end_row][end_col] == -1:
        return None

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distances: Dict[Tuple[int, int], int] = {}
    previous: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {}
    heap: List[Tuple[int, int, int]] = []

    for r in range(rows):
        for c in range(cols):
            distances[(r, c)] = float('inf')
            previous[(r, c)] = None

    distances[start] = 0
    heapq.heappush(heap, (0, start[0], start[1]))

    while heap:
        current_dist, r, c = heapq.heappop(heap)

        if (r, c) == end:
            break

        if current_dist > distances[(r, c)]:
            continue

        if grid[r][c] == -1:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == -1:
                    continue
                weight = grid[nr][nc]
                new_dist = current_dist + weight
                if new_dist < distances[(nr, nc)]:
                    distances[(nr, nc)] = new_dist
                    previous[(nr, nc)] = (r, c)
                    heapq.heappush(heap, (new_dist, nr, nc))

    if distances[end] == float('inf'):
        return None

    path: List[Tuple[int, int]] = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path, distances[end]

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1, 4, 1],
        [2, 1, 4, 1, 2],
        [1, 5, 1, 6, 1],
        [1, 2, 3, 4, 5]
    ]
    start_node = (0, 0)
    end_node = (3, 4)
    result = shortest_path_dijkstra(sample_grid, start_node, end_node)
    print(result)