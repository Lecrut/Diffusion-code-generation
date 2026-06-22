class MatrixFibonacci:
    BASE = [[1, 1], [1, 0]]
    IDENTITY = [[1, 0], [0, 1]]

    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def _mat_mul(self, A, B):
        a00, a01 = A[0][0], A[0][1]
        a10, a11 = A[1][0], A[1][1]
        b00, b01 = B[0][0], B[0][1]
        b10, b11 = B[1][0], B[1][1]
        return [
            [a00 * b00 + a01 * b10, a00 * b01 + a01 * b11],
            [a10 * b00 + a11 * b10, a10 * b01 + a11 * b11]
        ]

    def _mat_pow(self, base, exp):
        if exp == 0:
            return [[1, 0], [0, 1]]
        if exp == 1:
            return [row[:] for row in base]
        if exp % 2 == 0:
            half = self._mat_pow(base, exp // 2)
            return self._mat_mul(half, half)
        return self._mat_mul(base, self._mat_pow(base, exp - 1))

    def get_term(self, n):
        if n in self.cache:
            return self.cache[n]
        if n < 0:
            raise ValueError("Index must be non-negative")
        if n <= 1:
            return n
        if n == 2:
            return 1
        result_matrix = self._mat_pow(self.BASE, n - 1)
        value = result_matrix[0][0]
        self.cache[n] = value
        return value

if __name__ == '__main__':
    calculator = MatrixFibonacci()
    print(calculator.get_term(0))
    print(calculator.get_term(1))
    print(calculator.get_term(10))
    print(calculator.get_term(20))
    print(calculator.get_term(30))
    print(calculator.get_term(40))
    print(calculator.get_term(50))