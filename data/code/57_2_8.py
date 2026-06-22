import numpy as np

def matrix_mult(A, B):
    C = np.zeros((2, 2), dtype=np.int64)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_pow(M, n):
    if n == 1:
        return M
    if n % 2 == 0:
        half = matrix_pow(M, n // 2)
        return matrix_mult(half, half)
    else:
        return matrix_mult(M, matrix_pow(M, n - 1))

def compute_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    Q = np.array([[1, 1], [1, 0]], dtype=np.int64)
    Qn = matrix_pow(Q, n - 1)
    return Qn[0][0]

def compute_fibonacci_sequence(count):
    results = []
    for i in range(count):
        results.append(compute_fibonacci(i))
    return results

if __name__ == '__main__':
    sequence = compute_fibonacci_sequence(50)
    print(sequence)