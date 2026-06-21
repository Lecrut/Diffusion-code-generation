class MatrixProcessor:
    def __init__(self, matrix):
        self.matrix = matrix

    def is_reachable(self, start, end):
        rows, cols = len(self.matrix), len(self.matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or not self.matrix[r][c]:
                return False
            if (r, c) == end:
                return True
            visited[r][c] = True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                if dfs(r + dr, c + dc):
                    return True
            return False

        return dfs(start[0], start[1])

if __name__ == '__main__':
    processor = MatrixProcessor([[True, False, True],
                                 [False, True, False],
                                 [True, False, True]])
    
    result1 = processor.is_reachable((0, 0), (2, 2))
    print(result1)
    
    result2 = processor.is_reachable((0, 0), (2, 1))
    print(result2)