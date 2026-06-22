def matrix_multiply(a, b):
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
    ]

def matrix_power(matrix, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        n //= 2
    return result

def fibonacci_term(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    base_matrix = [[1, 1], [1, 0]]
    powered_matrix = matrix_power(base_matrix, n - 1)
    return powered_matrix[0][0]

def generate_fibonacci_sequence(count):
    return [fibonacci_term(i) for i in range(count)]

if __name__ == '__main__':
    first_50_fibonacci = generate_fibonacci_sequence(50)
    print(first_50_fibonacci)