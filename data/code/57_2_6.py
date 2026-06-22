def multiply(a, b):
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
    ]

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return multiply(half, half)
    else:
        return multiply(matrix, matrix_power(matrix, n - 1))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0][0]

def generate_fibonacci_sequence(count):
    return [fibonacci(i) for i in range(count)]

if __name__ == '__main__':
    terms = generate_fibonacci_sequence(50)
    for term in terms:
        print(term)