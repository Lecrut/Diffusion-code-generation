def validate_positive_integer(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Row count must be a positive integer")

def build_reverse_triangle(rows):
    validate_positive_integer(rows)
    lines = []
    for i in range(rows, 0, -1):
        sequence = list(range(1, i + 1))
        line_str = ' '.join(map(str, sequence))
        lines.append(line_str)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 6
    output = build_reverse_triangle(sample_size)
    print(output)