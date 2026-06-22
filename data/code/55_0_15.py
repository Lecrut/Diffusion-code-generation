def generate_right_aligned_alphabet_triangle(size):
    if not isinstance(size, int) or size <= 0:
        return []
    lines = []
    for i in range(1, size + 1):
        char = chr(ord('A') + i - 1)
        line = ' ' * (size - i) + char * i
        lines.append(line)
    return lines

if __name__ == '__main__':
    sample_values = 5
    result = generate_right_aligned_alphabet_triangle(sample_values)
    for line in result:
        print(line)