class MatrixFibonacci:
    def __init__(self):
        self.base = [[1, 1], [1, 0]]
        self.identity = [[1, 0], [0, 1]]

    def multiply(self, a, b):
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        ]

    def power(self, matrix, n):
        if n == 0:
            return self.identity
        if n == 1:
            return matrix
        half = self.power(matrix, n // 2)
        squared = self.multiply(half, half)
        if n % 2 == 0:
            return squared
        return self.multiply(squared, matrix)

    def compute_term(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        result = self.power(self.base, n - 1)
        return result[0][0]

if __name__ == '__main__':
    calculator = MatrixFibonacci()
    sample_indices = [0, 1, 2, 10, 20, 30, 40, 50]
    for idx in sample_indices:
        value = calculator.compute_term(idx)
        print(f"F({idx}) = {value}")