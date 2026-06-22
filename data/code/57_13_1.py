class FibonacciMatrix:
    def __init__(self, n):
        self.n = n

    def _matrix_mult(self, a, b):
        c00 = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        c01 = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        c10 = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        c11 = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return [[c00, c01], [c10, c11]]

    def _matrix_pow(self, base, exp):
        if exp == 1:
            return base
        if exp % 2 == 0:
            half = self._matrix_pow(base, exp // 2)
            return self._matrix_mult(half, half)
        else:
            return self._matrix_mult(base, self._matrix_pow(base, exp - 1))

    def get_term(self, index):
        if index == 0:
            return 0
        if index == 1:
            return 1
        if index > self.n:
            raise ValueError("Index exceeds maximum allowed term.")
        
        base_matrix = [[1, 1], [1, 0]]
        result_matrix = self._matrix_pow(base_matrix, index)
        return result_matrix[0][1]

if __name__ == '__main__':
    fib = FibonacciMatrix(50)
    print(fib.get_term(50))
    print(fib.get_term(10))
    print(fib.get_term(0))