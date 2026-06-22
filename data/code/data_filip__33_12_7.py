import heapq
from typing import List, Tuple, Optional

def dijkstra(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[Tuple[int, List[Tuple[int, int]]]]:
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

    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start_row][start_col] = 0
    predecessors = [[None] * cols for _ in range(rows)]

    pq = [(0, start_row, start_col)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        current_dist, r, c = heapq.heappop(pq)

        if r == end_row and c == end_col:
            break

        if current_dist > distances[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                weight = grid[nr][nc]
                new_dist = current_dist + weight
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    predecessors[nr][nc] = (r, c)
                    heapq.heappush(pq, (new_dist, nr, nc))

    if distances[end_row][end_col] == float('inf'):
        return None

    path = []
    current = (end_row, end_col)
    while current is not None:
        path.append(current)
        current = predecessors[current[0]][current[1]]

    path.reverse()
    return (distances[end_row][end_col], path)

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [2, 1, 4],
        [3, 2, 1]
    ]
    sample_start = (0, 0)
    sample_end = (2, 2)
    result = dijkstra(sample_grid, sample_start, sample_end)
    print(result)