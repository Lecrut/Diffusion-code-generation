class FibonacciCalculator:
    def __init__(self):
        self._memo = {0: 0, 1: 1}

    def _matrix_mult(self, A, B):
        rows_a = len(A)
        cols_a = len(A[0])
        cols_b = len(B[0])
        C = [[0] * cols_b for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def _matrix_pow(self, M, n):
        if n == 1:
            return [row[:] for row in M]
        if n % 2 == 0:
            half = self._matrix_pow(M, n // 2)
            return self._matrix_mult(half, half)
        else:
            return self._matrix_mult(M, self._matrix_pow(M, n - 1))

    def get_term(self, index):
        if index < 0:
            raise ValueError("Index must be non-negative")
        if index in self._memo:
            return self._memo[index]
        
        if index % 2 == 0:
            n = index // 2
            base_matrix = [[1, 1], [1, 0]]
            powered_matrix = self._matrix_pow(base_matrix, 2 * n)
            result = powered_matrix[0][1] + powered_matrix[1][1] 
            if index % 2 == 0:
                f_n_plus_1 = self._matrix_pow(base_matrix, n + 1)[0][0] if n > 0 else 1
                f_n = self._matrix_pow(base_matrix, n)[0][0] if n > 0 else 0
                self._memo[index] = f_n
                return f_n
            else:
                self._memo[index] = powered_matrix[0][1]
                return powered_matrix[0][1]
        else:
            n = (index - 1) // 2
            base_matrix = [[1, 1], [1, 0]]
            powered_matrix = self._matrix_pow(base_matrix, 2 * n)
            val = powered_matrix[0][0] + powered_matrix[0][1]
            self._memo[index] = val
            return val

        if index <= 1:
            return index
        
        base_matrix = [[1, 1], [1, 0]]
        powered_matrix = self._matrix_pow(base_matrix, index - 1)
        result = powered_matrix[0][0]
        self._memo[index] = result
        return result

if __name__ == '__main__':
    calc = FibonacciCalculator()
    print(calc.get_term(50))