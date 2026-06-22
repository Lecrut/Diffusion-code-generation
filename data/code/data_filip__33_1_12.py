import heapq

def dijkstra_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if not grid or not grid[0]:
        return float('inf'), []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dist = [[float('inf')] * cols for _ in range(rows)]
    prev = [[None] * cols for _ in range(rows)]

    dist[start[0]][start[1]] = 0

    pq = [(0, start)]

    while pq:
        current_dist, (r, c) = heapq.heappop(pq)

        if (r, c) == end:
            break

        if current_dist > dist[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = current_dist + grid[nr][nc]

                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    prev[nr][nc] = (r, c)
                    heapq.heappush(pq, (new_dist, (nr, nc)))

    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = prev[curr[0]][curr[1]]

    path.reverse()

    if dist[end[0]][end[1]] == float('inf'):
        return float('inf'), []

    return dist[end[0]][end[1]], path

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    start_point = (0, 0)
    end_point = (2, 2)

    shortest_distance, shortest_path = dijkstra_shortest_path(sample_grid, start_point, end_point)
    print(shortest_distance)
    print(shortest_path)