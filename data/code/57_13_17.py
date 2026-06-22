class FibonacciMatrixCalculator:
    def __init__(self):
        self.base_matrix = [[1, 1], [1, 0]]

    def multiply_matrices(self, A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def get_matrix_power(self, matrix, exp):
        if exp == 0:
            return [[1, 0], [0, 1]]
        if exp == 1:
            return matrix
        half_pow = self.get_matrix_power(matrix, exp // 2)
        squared = self.multiply_matrices(half_pow, half_pow)
        if exp % 2 == 0:
            return squared
        return self.multiply_matrices(squared, matrix)

    def get_fibonacci_term(self, index):
        if index < 0:
            raise ValueError("Index must be non-negative")
        if index == 0:
            return 0
        if index == 1:
            return 1
        power_matrix = self.get_matrix_power(self.base_matrix, index - 1)
        return power_matrix[0][0]

if __name__ == '__main__':
    calculator = FibonacciMatrixCalculator()
    print(calculator.get_fibonacci_term(50))
    print(calculator.get_fibonacci_term(10))
    print(calculator.get_fibonacci_term(0))