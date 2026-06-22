class FibonacciCalculator:
    def __init__(self):
        self.memo = {
            0: (0, 1),
            1: (1, 1)
        }

    def _matrix_mult(self, a, b):
        rows_a = len(a)
        cols_a = len(a[0])
        cols_b = len(b[0])
        result = [[0] * cols_b for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += a[i][k] * b[k][j]
        return result

    def _matrix_pow(self, matrix, power):
        result = [[1 if i == j else 0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        base = [row[:] for row in matrix]
        
        while power > 0:
            if power % 2 == 1:
                result = self._matrix_mult(result, base)
            base = self._matrix_mult(base, base)
            power //= 2
        return result

    def _get_pair(self, n):
        if n in self.memo:
            return self.memo[n]
        
        if n % 2 == 0:
            prev = self._get_pair(n // 2 - 1)
            f_prev = prev[0]
            f_curr = prev[1]
            f_n_minus_1 = f_prev + f_curr
            f_n = f_n_minus_1 + f_prev
        else:
            prev = self._get_pair(n - 1)
            f_prev = prev[0]
            f_curr = prev[1]
            f_n_minus_1 = f_curr
            f_n = f_prev + f_curr
        
        self.memo[n] = (f_n_minus_1, f_n)
        return self.memo[n]

    def get_term(self, n):
        if n < 0:
            raise ValueError("Index must be non-negative")
        if n == 0:
            return 0
        
        base_matrix = [[1, 1], [1, 0]]
        powered_matrix = self._matrix_pow(base_matrix, n)
        f_0 = 0
        f_1 = 1
        f_n = powered_matrix[0][0] * f_1 + powered_matrix[0][1] * f_0
        return f_n

    def get_sequence(self, n):
        seq = []
        for i in range(n + 1):
            seq.append(self.get_term(i))
        return seq

if __name__ == '__main__':
    calculator = FibonacciCalculator()
    print(calculator.get_term(50))
    print(calculator.get_term(10))