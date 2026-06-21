import heapq

def find_min_cost_path(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = matrix[0][0]
    pq = [(matrix[0][0], 0, 0)]
    while pq:
        current_cost, r, c = heapq.heappop(pq)
        if r == rows - 1 and c == cols - 1:
            return current_cost
        if current_cost > dist[r][c]:
            continue
        neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols:
                weight = matrix[nr][nc]
                new_cost = current_cost + weight
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
    return dist[rows - 1][cols - 1]
if __name__ == '__main__':
    sample_matrix = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = find_min_cost_path(sample_matrix)
    print(result)