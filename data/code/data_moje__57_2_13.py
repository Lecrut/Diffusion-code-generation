def matrix_mult(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

def matrix_pow(M, n):
    if n == 1:
        return M
    if n % 2 == 0:
        half = matrix_pow(M, n // 2)
        return matrix_mult(half, half)
    else:
        return matrix_mult(M, matrix_pow(M, n - 1))

def get_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 0
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(base_matrix, n - 1)
    return result_matrix[0][0]

def compute_first_50_fibonacci():
    terms = []
    for i in range(50):
        terms.append(get_fibonacci(i))
    return terms

if __name__ == '__main__':
    terms = compute_first_50_fibonacci()
    print(terms)