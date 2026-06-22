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

def fibonacci_matrix(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1)
    return result[0][0]

def get_first_n_fibonacci(n):
    return [fibonacci_matrix(i) for i in range(1, n + 1)]

if __name__ == '__main__':
    first_50 = get_first_n_fibonacci(50)
    print(first_50)