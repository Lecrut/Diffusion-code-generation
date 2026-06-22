class FibonacciEngine:
    TRANSITION = [[1, 1], [1, 0]]

    def multiply(self, x, y):
        a = x[0][0] * y[0][0] + x[0][1] * y[1][0]
        b = x[0][0] * y[0][1] + x[0][1] * y[1][1]
        c = x[1][0] * y[0][0] + x[1][1] * y[1][0]
        d = x[1][0] * y[0][1] + x[1][1] * y[1][1]
        return [[a, b], [c, d]]

    def exponentiate(self, base, power):
        if power == 0:
            return [[1, 0], [0, 1]]
        if power == 1:
            return [[base[0][0], base[0][1]], [base[1][0], base[1][1]]]
        half_res = self.exponentiate(base, power // 2)
        squared = self.multiply(half_res, half_res)
        if power % 2 == 0:
            return squared
        return self.multiply(squared, base)

    def calculate(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        result_matrix = self.exponentiate(self.TRANSITION, n - 1)
        return result_matrix[0][0]

if __name__ == '__main__':
    engine = FibonacciEngine()
    print(engine.calculate(0))
    print(engine.calculate(1))
    print(engine.calculate(10))
    print(engine.calculate(50))