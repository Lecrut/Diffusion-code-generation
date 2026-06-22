class FibonacciMatrix:
    BASE_MATRIX = [[1, 1], [1, 0]]
    IDENTITY_MATRIX = [[1, 0], [0, 1]]

    def _multiply(self, A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def _power(self, matrix, exp):
        if exp == 1:
            return matrix
        half = self._power(matrix, exp // 2)
        squared = self._multiply(half, half)
        if exp % 2 == 0:
            return squared
        return self._multiply(squared, matrix)

    def get_term(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 0
        result_matrix = self._power(self.BASE_MATRIX, n - 1)
        return result_matrix[0][0]

if __name__ == '__main__':
    calc = FibonacciMatrix()
    print(calc.get_term(10))
    print(calc.get_term(50))