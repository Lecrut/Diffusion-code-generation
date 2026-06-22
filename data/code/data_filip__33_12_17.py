import heapq

def dijkstra(grid, start, end):
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

    if grid[start[0]][start[1]] < 0 or grid[end[0]][end[1]] < 0:
        return None

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    previous = [[None] * cols for _ in range(rows)]

    heap = [(0, start[0], start[1])]
    visited = set()

    while heap:
        current_dist, r, c = heapq.heappop(heap)

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) == (end[0], end[1]):
            break

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                weight = grid[nr][nc]
                if weight < 0:
                    continue
                new_dist = current_dist + weight
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    previous[nr][nc] = (r, c)
                    heapq.heappush(heap, (new_dist, nr, nc))

    if distances[end[0]][end[1]] == float('inf'):
        return None

    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = previous[curr[0]][curr[1]]
    path.reverse()

    return path, distances[end[0]][end[1]]

if __name__ == '__main__':
    grid = [
        [1, 3, 1, 1],
        [1, 5, 1, 4],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    start_node = (0, 0)
    end_node = (3, 3)
    result = dijkstra(grid, start_node, end_node)
    print(result)