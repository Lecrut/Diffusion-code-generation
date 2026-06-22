class FibonacciCalculator:
    def __init__(self):
        self.cache = {}

    def multiply_matrices(self, A, B):
        C = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def power_matrix(self, M, n):
        if n == 1:
            return M
        if n % 2 == 0:
            half = self.power_matrix(M, n // 2)
            return self.multiply_matrices(half, half)
        else:
            return self.multiply_matrices(M, self.power_matrix(M, n - 1))

    def fibonacci(self, n):
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.cache:
            return self.cache[n]

        M = [[1, 1], [1, 0]]
        result_matrix = self.power_matrix(M, n)
        fib_n = result_matrix[0][1]
        self.cache[n] = fib_n
        return fib_n

if __name__ == '__main__':
    calc = FibonacciCalculator()
    print(calc.fibonacci(0))
    print(calc.fibonacci(1))
    print(calc.fibonacci(10))
    print(calc.fibonacci(20))
    print(calc.fibonacci(50))