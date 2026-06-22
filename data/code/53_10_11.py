def generate_reverse_number_triangle(n: int) -> str:
    lines = []
    for i in range(n, 0, -1):
        line = ' '.join((str(j) for j in range(1, i + 1)))
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    sample_value = 5
    result = generate_reverse_number_triangle(sample_value)
    print(result)