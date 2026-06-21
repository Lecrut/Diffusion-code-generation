import heapq

def dijkstra_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if rows == 0 or cols == 0:
        return None

    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None

    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return None

    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None

    distances = {}
    distances[start] = 0
    previous = {}
    previous[start] = None

    priority_queue = [(0, start)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = previous.get(node)
            path.reverse()
            return path

        if current_distance > distances.get(current_node, float('inf')):
            continue

        r, c = current_node
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_distance = current_distance + 1
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start_point = (0, 0)
    end_point = (4, 4)

    path = dijkstra_shortest_path(sample_grid, start_point, end_point)
    print(path)

    sample_grid_with_barrier = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]

    start_point_b = (0, 0)
    end_point_b = (2, 2)

    path_b = dijkstra_shortest_path(sample_grid_with_barrier, start_point_b, end_point_b)
    print(path_b)

    empty_grid = []
    path_c = dijkstra_shortest_path(empty_grid, (0, 0), (0, 0))
    print(path_c)

    blocked_start = [
        [1, 0],
        [0, 0]
    ]
    path_d = dijkstra_shortest_path(blocked_start, (0, 0), (1, 1))
    print(path_d)