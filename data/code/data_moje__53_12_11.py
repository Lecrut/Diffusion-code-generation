def build_reverse_number_triangle(size):
    if size <= 0:
        return []
    return [
        ''.join(str(j) for j in range(size - i + 1, 0, -1))
        for i in range(size, 0, -1)
    ]

def format_triangle(lines):
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 5
    triangle_lines = build_reverse_number_triangle(sample_size)
    print(format_triangle(triangle_lines))