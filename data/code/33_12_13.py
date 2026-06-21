import heapq

def dijkstra_shortest_path(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> tuple[float | None, list[tuple[int, int]]]:
    rows = len(grid)
    if rows == 0:
        return None, []
    cols = len(grid[0])
    if cols == 0:
        return None, []

    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None, []
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return None, []

    if grid[start[0]][start[1]] < 0 or grid[end[0]][end[1]] < 0:
        return None, []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dist = {}
    prev = {}
    visited = set()

    dist[start] = grid[start[0]][start[1]]
    prev[start] = None

    heap = [(grid[start[0]][start[1]], start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = prev[node]
            path.reverse()
            return current_dist, path

        r, c = current_node
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if (nr, nc) in visited:
                continue
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] < 0:
                continue

            weight = grid[nr][nc]
            new_dist = current_dist + weight
            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current_node
                heapq.heappush(heap, (new_dist, neighbor))

    if end in dist:
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = prev[node]
        path.reverse()
        return dist[end], path

    return None, []

if __name__ == '__main__':
    grid_sample = [
        [1, 2, 3],
        [4, 1, 6],
        [7, 8, 1]
    ]
    start_node = (0, 0)
    end_node = (2, 2)

    cost, path = dijkstra_shortest_path(grid_sample, start_node, end_node)

    print(cost)
    print(path)