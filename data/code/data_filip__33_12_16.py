import heapq

def dijkstra_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    if start is None or end is None:
        return None
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return None
    if grid[start[0]][start[1]] is None or grid[start[0]][start[1]] == -1:
        return None
    if grid[end[0]][end[1]] is None or grid[end[0]][end[1]] == -1:
        return None
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = grid[start[0]][start[1]]
    pq = [(dist[start[0]][start[1]], start[0], start[1])]
    while pq:
        current_dist, r, c = heapq.heappop(pq)
        if current_dist > dist[r][c]:
            continue
        if (r, c) == end:
            return current_dist
        for dr, dc in directions:
            nr, nc = (r + dr, c + dc)
            if 0 <= nr < rows and 0 <= nc < cols:
                cell_cost = grid[nr][nc]
                if cell_cost is not None and cell_cost != -1:
                    new_dist = current_dist + cell_cost
                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist
                        heapq.heappush(pq, (new_dist, nr, nc))
    return None
if __name__ == '__main__':
    sample_grid = [[0, 1, 2], [1, 0, 1], [2, 1, 0]]
    sample_start = (0, 0)
    sample_end = (2, 2)
    result = dijkstra_shortest_path(sample_grid, sample_start, sample_end)
    print(result)
    grid_with_obstacle = [[0, 1, 0], [1, -1, 1], [0, 1, 0]]
    result_blocked = dijkstra_shortest_path(grid_with_obstacle, (0, 0), (2, 2))
    print(result_blocked)
    empty_grid = []
    result_empty = dijkstra_shortest_path(empty_grid, None, None)
    print(result_empty)
    single_cell = [[5]]
    result_single = dijkstra_shortest_path(single_cell, (0, 0), (0, 0))
    print(result_single)
    unreachable_end = [[0, -1], [-1, 0]]
    result_unreachable = dijkstra_shortest_path(unreachable_end, (0, 0), (1, 1))
    print(result_unreachable)