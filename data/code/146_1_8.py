def matrix_mult(a, b):
    return [[sum(x*y for x, y in zip(row_a, col_b)) for col_b in zip(*b)] for row_a in a]

def matrix_pow(matrix, n):
    result = [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, matrix)
        matrix = matrix_mult(matrix, matrix)
        n //= 2
    return result

def fib(n):
    if n <= 1:
        return n
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1)
    return result[0][0]

if __name__ == '__main__':
    print(fib(50))