def generate_right_aligned_pyramid(n):
    lines = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        line = spaces + numbers
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_right_aligned_pyramid(5)
    print(result)