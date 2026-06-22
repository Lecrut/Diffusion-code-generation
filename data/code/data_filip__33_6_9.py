import heapq
from collections import defaultdict

def shortest_path_bfs(grid, start, end):
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])
    start_row, start_col = start
    end_row, end_col = end

    if grid[start_row][start_col] == 1 or grid[end_row][end_col] == 1:
        return -1

    if start == end:
        return 0

    visited = set()
    queue = [(start_row, start_col, 0)]
    visited.add((start_row, start_col))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        current_row, current_col, distance = queue.pop(0)

        if current_row == end_row and current_col == end_col:
            return distance

        for dr, dc in directions:
            nr, nc = current_row + dr, current_col + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, distance + 1))

    return -1

def shortest_path_dijkstra(grid, start, end):
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])
    start_row, start_col = start
    end_row, end_col = end

    if grid[start_row][start_col] == 1 or grid[end_row][end_col] == 1:
        return -1

    if start == end:
        return 0

    distance = [[float('inf')] * cols for _ in range(rows)]
    distance[start_row][start_col] = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    heap = [(0, start_row, start_col)]

    while heap:
        dist, current_row, current_col = heapq.heappop(heap)

        if current_row == end_row and current_col == end_col:
            return dist

        if dist > distance[current_row][current_col]:
            continue

        for dr, dc in directions:
            nr, nc = current_row + dr, current_col + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0:
                    new_dist = dist + 1
                    if new_dist < distance[nr][nc]:
                        distance[nr][nc] = new_dist
                        heapq.heappush(heap, (new_dist, nr, nc))

    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start = (0, 0)
    end = (3, 3)

    result_bfs = shortest_path_bfs(sample_grid, start, end)
    result_dijkstra = shortest_path_dijkstra(sample_grid, start, end)

    print(result_bfs)
    print(result_dijkstra)