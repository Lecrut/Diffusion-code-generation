import heapq

def dijkstra_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return None

    rows = len(grid)
    cols = len(grid[0])

    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return None

    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return None

    if grid[start[0]][start[1]] == -1 or grid[end[0]][end[1]] == -1:
        return None

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    visited = [[False] * cols for _ in range(rows)]

    priority_queue = [(0, start[0], start[1])]

    while priority_queue:
        current_dist, curr_row, curr_col = heapq.heappop(priority_queue)

        if visited[curr_row][curr_col]:
            continue

        visited[curr_row][curr_col] = True

        if (curr_row, curr_col) == end:
            return current_dist

        for dr, dc in directions:
            next_row = curr_row + dr
            next_col = curr_col + dc

            if (0 <= next_row < rows and 0 <= next_col < cols and
                    not visited[next_row][next_col] and
                    grid[next_row][next_col] != -1):
                weight = grid[next_row][next_col]
                new_dist = current_dist + weight

                if new_dist < distances[next_row][next_col]:
                    distances[next_row][next_col] = new_dist
                    heapq.heappush(priority_queue, (new_dist, next_row, next_col))

    return None

if __name__ == "__main__":
    sample_grid = [
        [1, 2, 3],
        [4, -1, 6],
        [7, 8, 9]
    ]

    start_pos = (0, 0)
    end_pos = (2, 2)

    result = dijkstra_shortest_path(sample_grid, start_pos, end_pos)
    print(result)

    sample_grid_obstacle = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result_clear = dijkstra_shortest_path(sample_grid_obstacle, (0, 0), (2, 2))
    print(result_clear)

    sample_grid_invalid_start = [
        [1, 2],
        [3, 4]
    ]

    result_invalid = dijkstra_shortest_path(sample_grid_invalid_start, (-1, 0), (1, 1))
    print(result_invalid)

    empty_grid = []
    result_empty = dijkstra_shortest_path(empty_grid, (0, 0), (0, 0))
    print(result_empty)