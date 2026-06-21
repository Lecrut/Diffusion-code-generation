class FibonacciCalculator:
    FIB_MATRIX = [[1, 1], [1, 0]]
    
    @staticmethod
    def matrix_mult(a, b):
        return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
    
    @classmethod
    def matrix_pow(cls, matrix, n):
        result = cls.FIB_MATRIX.copy()
        while n > 0:
            if n % 2 == 1:
                result = cls.matrix_mult(result, matrix)
            matrix = cls.matrix_mult(matrix, matrix)
            n //= 2
        return result
    
    @classmethod
    def fibonacci(cls, n):
        if n <= 1:
            return n
        powered_matrix = cls.matrix_pow(cls.FIB_MATRIX, n - 1)
        return powered_matrix[0][0]

if __name__ == '__main__':
    print(FibonacciCalculator.fibonacci(50))