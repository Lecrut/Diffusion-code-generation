def generate_centered_alphabet_triangle(n: int) -> list:
    if n <= 0:
        return []
    triangle = []
    for i in range(1, n + 1):
        letters = ''.join(chr(ord('A') + j) for j in range(i))
        padded = letters.center(2 * n - 1)
        triangle.append(padded)
    return triangle

if __name__ == '__main__':
    result = generate_centered_alphabet_triangle(5)
    print(result)