def matrix_mult(A, B):
    a = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    b = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    c = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    d = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return [[a, b], [c, d]]

def matrix_pow(M, p):
    if p == 1:
        return M
    if p % 2 == 0:
        half = matrix_pow(M, p // 2)
        return matrix_mult(half, half)
    return matrix_mult(M, matrix_pow(M, p - 1))

def get_fibonacci_terms(n):
    if n <= 0:
        return []
    fibs = []
    if n >= 1:
        fibs.append(0)
    if n >= 2:
        fibs.append(1)
    for i in range(2, n):
        base = [[1, 1], [1, 0]]
        res = matrix_pow(base, i - 1)
        fibs.append(res[0][0])
    return fibs

if __name__ == '__main__':
    terms = get_fibonacci_terms(50)
    for i, f in enumerate(terms):
        print(f"F({i}) = {f}")