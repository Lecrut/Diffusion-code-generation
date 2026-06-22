import heapq

def shortest_path_on_grid(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    if start == end:
        return 0

    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return -1
    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return -1
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return -1

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0
    pq = [(0, start[0], start[1])]

    while pq:
        d, r, c = heapq.heappop(pq)
        if (r, c) == end:
            return d
        if d > dist[r][c]:
            continue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_dist = d + 1
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))

    return -1

if __name__ == '__main__':
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start = (0, 0)
    end = (2, 2)
    print(shortest_path_on_grid(grid, start, end))