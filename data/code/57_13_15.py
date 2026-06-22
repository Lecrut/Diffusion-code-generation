class FibonacciCalculator:
    def __init__(self):
        self.cache = {}

    def _matrix_mult(self, A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def _matrix_pow(self, M, n):
        if n == 1:
            return M
        if n % 2 == 0:
            half = self._matrix_pow(M, n // 2)
            return self._matrix_mult(half, half)
        else:
            return self._matrix_mult(M, self._matrix_pow(M, n - 1))

    def nth_fibonacci(self, n):
        if n in self.cache:
            return self.cache[n]
        if n < 0:
            raise ValueError("Index must be non-negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        M = [[1, 1], [1, 0]]
        result_matrix = self._matrix_pow(M, n)
        result = result_matrix[0][1]
        self.cache[n] = result
        return result

if __name__ == '__main__':
    calc = FibonacciCalculator()
    for i in [0, 1, 5, 10, 20, 50]:
        print(f"F({i}) = {calc.nth_fibonacci(i)}")