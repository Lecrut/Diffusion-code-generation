class FibonacciMatrix:
    def __init__(self):
        self.matrix = [[1, 1], [1, 0]]

    def multiply_matrices(self, A, B):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def power(self, matrix, p):
        if p == 1:
            return matrix
        if p % 2 == 0:
            half = self.power(matrix, p // 2)
            return self.multiply_matrices(half, half)
        else:
            half = self.power(matrix, (p - 1) // 2)
            squared = self.multiply_matrices(half, half)
            return self.multiply_matrices(squared, matrix)

    def get_fibonacci(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        result_matrix = self.power(self.matrix, n)
        return result_matrix[0][1]

if __name__ == '__main__':
    fib = FibonacciMatrix()
    indices_to_check = [0, 1, 2, 3, 10, 20, 50]
    for n in indices_to_check:
        print(fib.get_fibonacci(n))