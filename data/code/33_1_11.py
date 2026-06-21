import heapq
from typing import List, Tuple, Optional, Dict

def dijkstra_shortest_path(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[int]:
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return None

    if grid[start[0]][start[1]] == 1:
        return None
    if grid[end[0]][end[1]] == 1:
        return None

    if start == end:
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist_map: Dict[Tuple[int, int], int] = {}
    dist_map[start] = 0
    priority_queue: List[Tuple[int, Tuple[int, int]]] = [(0, start)]
    visited: set = set()

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            return current_dist

        x, y = current_node
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 1:
                    continue
                if (nx, ny) in visited:
                    continue
                
                new_dist = current_dist + 1
                if (nx, ny) not in dist_map or new_dist < dist_map[(nx, ny)]:
                    dist_map[(nx, ny)] = new_dist
                    heapq.heappush(priority_queue, (new_dist, (nx, ny)))

    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    result = dijkstra_shortest_path(sample_grid, start_node, end_node)
    print(result)