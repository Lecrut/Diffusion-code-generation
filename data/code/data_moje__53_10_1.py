def generate_reverse_number_triangle(n: int) -> str:
    lines = []
    for i in range(n, 0, -1):
        row_numbers = range(1, i + 1)
        line = ' '.join(str(num) for num in row_numbers)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    n = 5
    result = generate_reverse_number_triangle(n)
    print(result)