class FibonacciCalculator:
    FIB_MATRIX = [[1, 1], [1, 0]]

    @staticmethod
    def matrix_mult(a, b):
        return [
            [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a
        ]

    @staticmethod
    def matrix_pow(matrix, n):
        result = [[1, 0], [0, 1]]
        while n > 0:
            if n % 2 == 1:
                result = FibonacciCalculator.matrix_mult(result, matrix)
            matrix = FibonacciCalculator.matrix_mult(matrix, matrix)
            n //= 2
        return result

    def fibonacci(self, n):
        if n <= 1:
            return n
        powered_matrix = self.matrix_pow(self.FIB_MATRIX, n - 1)
        return powered_matrix[0][0]

if __name__ == '__main__':
    calculator = FibonacciCalculator()
    print(calculator.fibonacci(50))