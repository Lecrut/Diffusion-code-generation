import collections
import heapq

def shortest_path(grid):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
    if start is None or end is None:
        return None
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = [(0, start)]
    visited = set()
    visited.add(start)
    while heap:
        dist, (r, c) = heapq.heappop(heap)
        if (r, c) == end:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (dist + 1, (nr, nc)))
    return None

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', '#'],
        ['#', '.', '#', '.'],
        ['.', '.', '.', 'E']
    ]
    result = shortest_path(sample_grid)
    print(result)