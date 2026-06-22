def matrix_mult(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def matrix_pow(M, n):
    if n == 1:
        return M
    if n % 2 == 0:
        half = matrix_pow(M, n // 2)
        return matrix_mult(half, half)
    else:
        return matrix_mult(M, matrix_pow(M, n - 1))

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    M = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(M, n)
    return result_matrix[0][1]

if __name__ == '__main__':
    fib_50 = [fibonacci(i) for i in range(1, 51)]
    print(fib_50)