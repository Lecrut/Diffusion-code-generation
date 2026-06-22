class MatrixFibonacci:
    BASE = [[1, 1], [1, 0]]

    def _multiply(self, a, b):
        a00, a01, a10, a11 = a[0][0], a[0][1], a[1][0], a[1][1]
        b00, b01, b10, b11 = b[0][0], b[0][1], b[1][0], b[1][1]
        return [
            [a00 * b00 + a01 * b10, a00 * b01 + a01 * b11],
            [a10 * b00 + a11 * b10, a10 * b01 + a11 * b11]
        ]

    def _pow(self, base, n):
        if n == 0:
            return [[1, 0], [0, 1]]
        if n == 1:
            return [row[:] for row in base]
        half = self._pow(base, n // 2)
        result = self._multiply(half, half)
        if n % 2 == 1:
            result = self._multiply(result, base)
        return result

    def get_n(self, n):
        if n < 0:
            raise ValueError("Index must be non-negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        base = [row[:] for row in self.BASE]
        matrix_n = self._pow(base, n)
        return matrix_n[0][1]

if __name__ == '__main__':
    calculator = MatrixFibonacci()
    indices = [0, 1, 2, 5, 10, 20, 30, 40, 50]
    for idx in indices:
        print(calculator.get_n(idx))