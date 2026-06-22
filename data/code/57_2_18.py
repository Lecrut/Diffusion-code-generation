def multiply_matrices(A, B):
    a00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    a01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    a10 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    a11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return [[a00, a01], [a10, a11]]

def power_matrix(M, n):
    if n == 1:
        return M
    if n % 2 == 0:
        half = power_matrix(M, n // 2)
        return multiply_matrices(half, half)
    else:
        return multiply_matrices(M, power_matrix(M, n - 1))

def compute_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 0
    base = [[1, 1], [1, 0]]
    result_matrix = power_matrix(base, n)
    return result_matrix[0][1]

if __name__ == '__main__':
    fib_terms = []
    for i in range(1, 51):
        fib_terms.append(compute_fibonacci(i))
    print(fib_terms)