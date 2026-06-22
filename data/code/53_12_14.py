def generate_reverse_number_triangle(size):
    if size <= 0:
        return ""
    lines = []
    for i in range(size, 0, -1):
        numbers = list(range(1, i + 1))
        line = ' '.join(map(str, numbers))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 5
    result = generate_reverse_number_triangle(sample_size)
    print(result)