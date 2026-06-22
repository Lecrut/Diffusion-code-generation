class FibMatrix:
    def multiply(self, a, b):
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        ]

    def pow(self, base, exp):
        if exp == 1:
            return [row[:] for row in base]
        if exp == 0:
            return [[1, 0], [0, 1]]
        half = self.pow(base, exp // 2)
        squared = self.multiply(half, half)
        if exp % 2 == 0:
            return squared
        return self.multiply(squared, base)

    def nth(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        base = [[1, 1], [1, 0]]
        result = self.pow(base, n - 1)
        return result[0][0]

if __name__ == '__main__':
    calculator = FibMatrix()
    sample_indices = [0, 1, 5, 10, 20, 30, 40, 50]
    for idx in sample_indices:
        print(calculator.nth(idx))