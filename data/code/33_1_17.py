import heapq
from typing import List, Tuple, Optional

def dijkstra_shortest_path(
    grid: List[List[int]],
    start: Tuple[int, int],
    end: Tuple[int, int]
) -> Optional[int]:
    rows = len(grid)
    if rows == 0:
        return None
    cols = len(grid[0])
    if cols == 0:
        return None

    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return None

    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return None

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = grid[start[0]][start[1]]

    heap = [(grid[start[0]][start[1]], start[0], start[1])]

    visited = [[False] * cols for _ in range(rows)]

    while heap:
        current_dist, r, c = heapq.heappop(heap)

        if r == end[0] and c == end[1]:
            return current_dist

        if visited[r][c]:
            continue
        visited[r][c] = True

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] != 0:
                new_dist = current_dist + grid[nr][nc]
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(heap, (new_dist, nr, nc))

    return None

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    start_pos = (0, 0)
    end_pos = (2, 2)
    result = dijkstra_shortest_path(sample_grid, start_pos, end_pos)
    print(result)

    blocked_grid = [
        [1, 0, 1],
        [1, 1, 1],
        [0, 2, 1]
    ]
    result_blocked = dijkstra_shortest_path(blocked_grid, (0, 0), (2, 2))
    print(result_blocked)

    unreachable_grid = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    result_unreachable = dijkstra_shortest_path(unreachable_grid, (0, 0), (2, 2))
    print(result_unreachable)