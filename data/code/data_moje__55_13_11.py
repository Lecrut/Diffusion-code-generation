def generate_triangular_pattern(rows):
    pattern_lines = []
    for i in range(1, rows + 1):
        line = ""
        for j in range(i):
            line += chr(ord('A') + (i + j) % 26)
        pattern_lines.append(line)
    return "\n".join(pattern_lines)

if __name__ == '__main__':
    sample_rows = 5
    result = generate_triangular_pattern(sample_rows)
    print(result)