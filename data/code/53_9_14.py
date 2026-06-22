def print_reverse_number_triangle(height=5):
    lines = []
    for i in range(height, 0, -1):
        line = ' '.join(str(i) for _ in range(i))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = print_reverse_number_triangle(5)
    print(result)