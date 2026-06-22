def generate_pyramid_pattern(n):
    lines = []
    for i in range(1, n + 1):
        prefix_spaces = ' ' * (n - i)
        alpha_chars = [chr(ord('A') + j) for j in range(i)]
        line_content = ''.join(alpha_chars)
        lines.append(f"{prefix_spaces}{line_content}")
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_pyramid_pattern(5)
    print(result)