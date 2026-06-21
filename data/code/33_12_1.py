import heapq

def dijkstra(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        raise ValueError("Start point is out of bounds.")
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        raise ValueError("End point is out of bounds.")
    if grid[start[0]][start[1]] == float('inf'):
        raise ValueError("Start point is blocked.")
    if grid[end[0]][end[1]] == float('inf'):
        raise ValueError("End point is blocked.")
    if start == end:
        return 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    priority_queue = [(0, start)]
    distances = {}
    distances[start] = 0
    while priority_queue:
        current_distance, current_pos = heapq.heappop(priority_queue)
        if current_pos in visited:
            continue
        if current_pos == end:
            return current_distance
        visited.add(current_pos)
        r, c = current_pos
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == float('inf'):
                    continue
                neighbor = (nr, nc)
                weight = grid[nr][nc]
                new_distance = current_distance + weight
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    return float('inf')

if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [float('inf'), 1, 1],
        [1, 1, 1]
    ]
    start = (0, 0)
    end = (2, 2)
    result = dijkstra(grid, start, end)
    print(result)