import heapq

def shortest_path_binary_grid(grid, start, end):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    if start == end:
        return [start]

    queue = [(0, start)]
    visited = set()
    visited.add(start)
    parent = {start: None}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        dist, current = heapq.heappop(queue)
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for dr, dc in directions:
            r, c = current[0] + dr, current[1] + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and (r, c) not in visited:
                visited.add((r, c))
                parent[(r, c)] = current
                heapq.heappush(queue, (dist + 1, (r, c)))
    return None

if __name__ == '__main__':
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    result = shortest_path_binary_grid(grid, start, end)
    print(result)