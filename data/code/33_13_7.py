import heapq

def shortest_path_binary_matrix(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1
    if rows == 1 and cols == 1:
        return 1

    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = 1
    heap = [(1, 0, 0)]

    while heap:
        d, r, c = heapq.heappop(heap)
        if r == rows - 1 and c == cols - 1:
            return d
        if d > dist[r][c]:
            continue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_dist = d + 1
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(heap, (new_dist, nr, nc))
    return -1

if __name__ == '__main__':
    grid = [
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0]
    ]
    print(shortest_path_binary_matrix(grid))