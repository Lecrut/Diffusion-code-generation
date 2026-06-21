import heapq

def dijkstra_shortest_path(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> int:
    rows = len(grid)
    if rows == 0:
        return -1
    cols = len(grid[0])
    if cols == 0:
        return -1

    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return -1
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return -1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = grid[start[0]][start[1]]
    pq = [(dist[start[0]][start[1]], start)]
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        r, c = current_node

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            return current_dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                new_dist = current_dist + grid[nr][nc]
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, (nr, nc)))

    return -1

if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    start_pos = (0, 0)
    end_pos = (2, 2)
    result = dijkstra_shortest_path(grid, start_pos, end_pos)
    print(result)