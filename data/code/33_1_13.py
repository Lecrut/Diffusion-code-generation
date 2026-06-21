import heapq

def shortest_path_on_grid(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    priority_queue = [(0, start[0], start[1])]
    while priority_queue:
        current_dist, r, c = heapq.heappop(priority_queue)
        if (r, c) == end:
            return distances[r][c]
        if current_dist > distances[r][c]:
            continue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                new_dist = current_dist + grid[nr][nc]
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    heapq.heappush(priority_queue, (new_dist, nr, nc))
    return -1

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    start_pos = (0, 0)
    end_pos = (2, 2)
    result = shortest_path_on_grid(sample_grid, start_pos, end_pos)
    print(result)