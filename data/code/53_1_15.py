def generate_right_aligned_reverse_triangle(n):
    lines = []
    for i in range(n, 0, -1):
        nums = ' '.join(str(j) for j in range(1, i + 1))
        line = ' ' * (2 * (n - i)) + nums
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_right_aligned_reverse_triangle(4)
    print(result)