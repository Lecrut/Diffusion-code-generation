def generate_right_aligned_triangle(n):
    lines = []
    for i in range(1, n + 1):
        letters = ''.join(chr(ord('A') + j) for j in range(i))
        spaces = ' ' * (n - i)
        lines.append(spaces + letters)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_n = 5
    result = generate_right_aligned_triangle(sample_n)
    print(result)