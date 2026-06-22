def matrix_mult(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_pow(M, p):
    n = len(M)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1
    base = [row[:] for row in M]
    while p > 0:
        if p % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        p //= 2
    return result

def fibonacci_matrix(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    M = [[1, 1], [1, 0]]
    M_n = matrix_pow(M, n - 1)
    return M_n[0][0]

def first_n_fibonacci(n):
    return [fibonacci_matrix(i) for i in range(1, n + 1)]

if __name__ == '__main__':
    result = first_n_fibonacci(50)
    print(result)