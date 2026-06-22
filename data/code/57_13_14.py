class FibonacciMatrix:
    def __init__(self):
        self.memo = {}

    def matrix_multiply(self, a, b):
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        ]

    def matrix_power(self, matrix, n):
        if n == 0:
            return [[1, 0], [0, 1]]
        if n == 1:
            return matrix
        if n % 2 == 0:
            half = self.matrix_power(matrix, n // 2)
            return self.matrix_multiply(half, half)
        else:
            return self.matrix_multiply(matrix, self.matrix_power(matrix, n - 1))

    def calculate(self, n):
        if n < 0:
            raise ValueError("Index must be non-negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        base_matrix = [[1, 1], [1, 0]]
        result_matrix = self.matrix_power(base_matrix, n - 1)
        return result_matrix[0][0]

if __name__ == '__main__':
    fib_calc = FibonacciMatrix()
    sample_indices = [0, 1, 2, 5, 10, 20, 50]
    for index in sample_indices:
        print(index, fib_calc.calculate(index))