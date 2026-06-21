import heapq

def dijkstra(grid, start, end):
    if not grid or not grid[0]:
        return None, 0

    rows = len(grid)
    cols = len(grid[0])

    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None, 0
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return None, 0

    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return None, 0

    distance = [[float('inf')] * cols for _ in range(rows)]
    distance[start[0]][start[1]] = 0
    previous = [[None] * cols for _ in range(rows)]

    pq = [(0, start[0], start[1])]
    visited = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        dist, r, c = heapq.heappop(pq)

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if (r, c) == end:
            break

        current_dist = distance[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                new_dist = current_dist + 1
                if new_dist < distance[nr][nc]:
                    distance[nr][nc] = new_dist
                    previous[nr][nc] = (r, c)
                    heapq.heappush(pq, (new_dist, nr, nc))

    path = []
    current = end
    if distance[end[0]][end[1]] == float('inf'):
        return None, 0

    while current is not None:
        path.append(current)
        current = previous[current[0]][current[1]]

    path.reverse()

    return path, distance[end[0]][end[1]]

if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    start = (0, 0)
    end = (4, 4)
    path, distance = dijkstra(grid, start, end)
    print(path)
    print(distance)