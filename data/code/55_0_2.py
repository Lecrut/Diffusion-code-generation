def generate_right_aligned_alphabet_triangle(n: int) -> list[str]:
    if not isinstance(n, int) or n <= 0 or n > 26:
        return []
    result = []
    for i in range(n):
        chars = [chr(65 + j) for j in range(i + 1)]
        line = ''.join(chars)
        result.append(line.rjust(n))
    return result
if __name__ == '__main__':
    n = 5
    triangle = generate_right_aligned_alphabet_triangle(n)
    for line in triangle:
        print(line)