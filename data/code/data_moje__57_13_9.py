class FibonacciCalculator:
    def __init__(self):
        self.cache = {}

    def _matrix_mult(self, A, B):
        C = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
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

    def nth_fibonacci(self, n):
        if n < 0:
            raise ValueError("Index must be non-negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.cache:
            return self.cache[n]

        base_matrix = [[1, 1], [1, 0]]
        result_matrix = self._matrix_pow(base_matrix, n - 1)
        fib_n = result_matrix[0][0]

        self.cache[n] = fib_n
        return fib_n

if __name__ == '__main__':
    calc = FibonacciCalculator()
    indices = [0, 1, 2, 5, 10, 20, 30, 40, 50]
    for idx in indices:
        print(calc.nth_fibonacci(idx))