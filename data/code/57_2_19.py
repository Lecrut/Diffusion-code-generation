import math

def mat_mult(A, B):
    C = [[0, 0], [0, 0]]
    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return C

def mat_pow(M, p):
    if p == 1:
        return M
    if p % 2 == 0:
        half = mat_pow(M, p // 2)
        return mat_mult(half, half)
    return mat_mult(M, mat_pow(M, p - 1))

def fib_matrix(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    base = [[1, 1], [1, 0]]
    result = mat_pow(base, n)
    return result[0][1]

def compute_fibonacci_series(count):
    if count <= 0:
        return []
    series = []
    for i in range(count):
        series.append(fib_matrix(i))
    return series

if __name__ == '__main__':
    count = 50
    result = compute_fibonacci_series(count)
    print(result)