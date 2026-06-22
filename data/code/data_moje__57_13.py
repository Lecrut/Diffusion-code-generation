class FibonacciCalculator:
    def __init__(self):
        self.memo = {}

    def multiply_matrices(self, A, B):
        C = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def power(self, matrix, n):
        if n == 1:
            return matrix
        if n % 2 == 0:
            half = self.power(matrix, n // 2)
            return self.multiply_matrices(half, half)
        else:
            return self.multiply_matrices(matrix, self.power(matrix, n - 1))

    def nth_fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        F = [[1, 1], [1, 0]]
        result_matrix = self.power(F, n - 1)
        return result_matrix[0][0]

if __name__ == '__main__':
    calc = FibonacciCalculator()
    print(calc.nth_fibonacci(10))
    print(calc.nth_fibonacci(20))
    print(calc.nth_fibonacci(50))