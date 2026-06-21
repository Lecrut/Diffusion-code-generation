import heapq

def dijkstra_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return None

    rows = len(grid)
    cols = len(grid[0])

    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return None

    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return None

    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    previous = [[None] * cols for _ in range(rows)]

    priority_queue = [(0, start)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while priority_queue:
        current_dist, current_pos = heapq.heappop(priority_queue)

        if current_pos == end:
            break

        if current_dist > distances[current_pos[0]][current_pos[1]]:
            continue

        for dr, dc in directions:
            new_row, new_col = current_pos[0] + dr, current_pos[1] + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                distance = current_dist + 1

                if distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = distance
                    previous[new_row][new_col] = current_pos
                    heapq.heappush(priority_queue, (distance, (new_row, new_col)))

    if distances[end[0]][end[1]] == float('inf'):
        return None

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current[0]][current[1]]

    path.reverse()
    return path

if __name__ == '__main__':
    sample_grid = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1]
    ]
    start_point = (0, 0)
    end_point = (3, 4)

    result = dijkstra_shortest_path(sample_grid, start_point, end_point)
    print(result)