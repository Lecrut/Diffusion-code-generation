class FibonacciMatrix:
    def __init__(self):
        self.memo = {}

    def multiply(self, a, b):
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        ]

    def power(self, matrix, n):
        if n == 1:
            return matrix
        if n % 2 == 0:
            half = self.power(matrix, n // 2)
            return self.multiply(half, half)
        else:
            return self.multiply(self.power(matrix, n - 1), matrix)

    def calculate(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        base_matrix = [[1, 1], [1, 0]]
        result_matrix = self.power(base_matrix, n - 1)
        return result_matrix[0][0]

if __name__ == '__main__':
    fib_calc = FibonacciMatrix()
    print(fib_calc.calculate(50))
    print(fib_calc.calculate(10))
    print(fib_calc.calculate(0))
    print(fib_calc.calculate(1))
    print(fib_calc.calculate(2))