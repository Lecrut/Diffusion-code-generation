def multiply(A, B):
    a = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    b = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    c = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    d = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return ((a, b), (c, d))

def identity_matrix():
    return ((1, 0), (0, 1))

def matrix_power(M, n):
    if n == 0:
        return identity_matrix()
    if n == 1:
        return M
    half = matrix_power(M, n // 2)
    if n % 2 == 0:
        return multiply(half, half)
    else:
        return multiply(multiply(half, half), M)

def compute_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    base_matrix = ((1, 1), (1, 0))
    result_matrix = matrix_power(base_matrix, n)
    return result_matrix[0][1]

def get_first_n_fibonacci_terms(count):
    terms = []
    for i in range(1, count + 1):
        terms.append(compute_fibonacci(i))
    return terms

if __name__ == '__main__':
    fib_terms = get_first_n_fibonacci_terms(50)
    for index, value in enumerate(fib_terms):
        print(f"{index + 1}: {value}")