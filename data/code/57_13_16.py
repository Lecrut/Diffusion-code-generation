class FibonacciMatrix:
    def __init__(self):
        self._cache = {0: 0, 1: 1}

    def _matrix_multiply(self, a, b):
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ]

    def _matrix_power(self, matrix, n):
        result = [[1, 0], [0, 1]]
        base = matrix
        while n > 0:
            if n % 2 == 1:
                result = self._matrix_multiply(result, base)
            base = self._matrix_multiply(base, base)
            n //= 2
        return result

    def calculate(self, n):
        if n in self._cache:
            return self._cache[n]
        if n < 0:
            raise ValueError("Index must be non-negative")
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        base_matrix = [[1, 1], [1, 0]]
        powered_matrix = self._matrix_power(base_matrix, n - 1)
        result = powered_matrix[0][0]
        self._cache[n] = result
        return result

if __name__ == '__main__':
    fib_calc = FibonacciMatrix()
    sample_indices = [0, 1, 10, 20, 30, 40, 50]
    for index in sample_indices:
        print(f"F({index}) = {fib_calc.calculate(index)}")