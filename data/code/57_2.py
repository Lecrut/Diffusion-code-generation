def matrix_multiply(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_power(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    if n == 1:
        return matrix
    half_power = matrix_power(matrix, n // 2)
    result = matrix_multiply(half_power, half_power)
    if n % 2 == 1:
        result = matrix_multiply(result, matrix)
    return result

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    base_matrix = [[1, 1], [1, 0]]
    powered_matrix = matrix_power(base_matrix, n - 1)
    return powered_matrix[0][0]

if __name__ == '__main__':
    first_50_terms = []
    for i in range(50):
        first_50_terms.append(fibonacci(i))
    for index, value in enumerate(first_50_terms):
        print(f"F({index}) = {value}")