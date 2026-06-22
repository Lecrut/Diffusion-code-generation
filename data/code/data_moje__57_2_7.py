def matrix_mult(A, B):
    c00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    c01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    c10 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    c11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return [[c00, c01], [c10, c11]]

def matrix_pow(M, n):
    if n == 1:
        return M
    if n % 2 == 0:
        half = matrix_pow(M, n // 2)
        return matrix_mult(half, half)
    else:
        return matrix_mult(M, matrix_pow(M, n - 1))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    base = [[1, 1], [1, 0]]
    result = matrix_pow(base, n)
    return result[0][1]

if __name__ == '__main__':
    terms = []
    for i in range(50):
        terms.append(fib(i))
    for idx, val in enumerate(terms):
        print(f"Fib({idx}) = {val}")