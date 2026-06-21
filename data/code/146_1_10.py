class FibonacciCalculator:
    def __init__(self):
        self.fib_matrix = [[1, 1], [1, 0]]

    def matrix_mult(self, a, b):
        return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]

    def matrix_pow(self, matrix, n):
        result = [[1, 0], [0, 1]]
        while n > 0:
            if n % 2 == 1:
                result = self.matrix_mult(result, matrix)
            matrix = self.matrix_mult(matrix, matrix)
            n //= 2
        return result

    def fibonacci(self, n):
        if n <= 1:
            return n
        powered_matrix = self.matrix_pow(self.fib_matrix, n - 1)
        return powered_matrix[0][0]

if __name__ == '__main__':
    calculator = FibonacciCalculator()
    print(calculator.fibonacci(50))