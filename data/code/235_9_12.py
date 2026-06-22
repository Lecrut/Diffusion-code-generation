def generate_line_pattern(n):
    pattern = []
    for i in range(n):
        line = "*" * (2 * i + 1)
        pattern.append(line)
    return "\n".join(pattern)

if __name__ == '__main__':
    sample_pattern = generate_line_pattern(5)
    print(sample_pattern)