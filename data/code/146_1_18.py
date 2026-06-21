def matrix_mult(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]

def matrix_pow(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n % 2 == 0:
        half_power = matrix_pow(matrix, n // 2)
        return matrix_mult(half_power, half_power)
    else:
        return matrix_mult(matrix, matrix_pow(matrix, n - 1))

def fibonacci(n):
    if n <= 1:
        return n
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(fib_matrix, n - 1)
    return result_matrix[0][0]

if __name__ == '__main__':
    print(fibonacci(50))