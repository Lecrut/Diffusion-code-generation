def print_reverse_number_triangle(height: int) -> str:
    if height <= 0:
        return ''
    lines = []
    for i in range(height, 0, -1):
        row_numbers = []
        for j in range(1, i + 1):
            row_numbers.append(str(j))
        lines.append(' '.join(row_numbers))
    return '\n'.join(lines)
if __name__ == '__main__':
    HEIGHT = 5
    result = print_reverse_number_triangle(HEIGHT)
    print(result)