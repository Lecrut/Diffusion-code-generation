import sys

def matrix_mult(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]], [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

def matrix_pow(M, n):
    if n == 1:
        return M
    if n % 2 == 0:
        half = matrix_pow(M, n // 2)
        return matrix_mult(half, half)
    else:
        return matrix_mult(M, matrix_pow(M, n - 1))

def compute_fibonacci_terms(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    if n >= 3:
        base_matrix = [[1, 1], [1, 0]]
        for k in range(2, n):
            if k == 2:
                result_matrix = matrix_pow(base_matrix, k - 1)
                fibs.append(result_matrix[0][0])
            else:
                prev_matrix = [[fibs[k - 2], fibs[k - 3]], [fibs[k - 3], fibs[k - 4]]]
    results = []
    for i in range(1, n + 1):
        if i == 1:
            results.append(0)
            continue
        if i == 2:
            results.append(1)
            continue
        M = [[1, 1], [1, 0]]
        power_matrix = matrix_pow(M, i - 1)
        fib_val = power_matrix[0][1]
        results.append(fib_val)
    return results
if __name__ == '__main__':
    terms = compute_fibonacci_terms(50)
    print(terms)