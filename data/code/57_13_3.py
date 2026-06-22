class FibonacciMatrix:
    def __init__(self, n):
        self.index = n

    def multiply(self, A, B):
        c00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        c01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        c10 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        c11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]
        return [[c00, c01], [c10, c11]]

    def power(self, base, exp):
        if exp == 1:
            return base
        if exp % 2 == 0:
            half = self.power(base, exp // 2)
            return self.multiply(half, half)
        else:
            return self.multiply(base, self.power(base, exp - 1))

    def get_term(self):
        if self.index == 0:
            return 0
        if self.index == 1:
            return 1
        base_matrix = [[1, 1], [1, 0]]
        result_matrix = self.power(base_matrix, self.index - 1)
        return result_matrix[0][0]

if __name__ == '__main__':
    fib_calc = FibonacciMatrix(50)
    print(fib_calc.get_term())