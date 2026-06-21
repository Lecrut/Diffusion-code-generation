def matrix_multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]

def matrix_power(matrix, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        n //= 2
    return result

def fibonacci(n):
    if n <= 1:
        return n
    fib_matrix = [[1, 1], [1, 0]]
    powered_matrix = matrix_power(fib_matrix, n - 1)
    return powered_matrix[0][0]

if __name__ == '__main__':
    nth_fibonacci = fibonacci(50)
    print(nth_fibonacci)