def generate_pattern(n):
    lines = []
    for i in range(1, n + 1):
        lines.append("*" * i)
    return "\n".join(lines)
if __name__ == '__main__':
    sample_number = 5
    pattern = generate_pattern(sample_number)
    print(pattern)