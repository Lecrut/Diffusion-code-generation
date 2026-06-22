import heapq
from typing import List, Tuple

def find_min_cost_path(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = grid[start[0]][start[1]]
    pq = [(distances[start[0]][start[1]], start)]
    
    while pq:
        current_dist, (r, c) = heapq.heappop(pq)
        if r == end[0] and c == end[1]:
            return current_dist
        if current_dist > distances[r][c]:
            continue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = current_dist + grid[nr][nc]
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, (nr, nc)))
    return -1

if __name__ == '__main__':
    sample_grid = [
        [5, 3, 4],
        [2, 1, 3],
        [6, 8, 1]
    ]
    start_pos = (0, 0)
    end_pos = (2, 2)
    result = find_min_cost_path(sample_grid, start_pos, end_pos)
    print(result)