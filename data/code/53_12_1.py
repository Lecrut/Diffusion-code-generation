def reverse_number_triangle(size):
    lines = []
    for row in range(size, 0, -1):
        numbers = [str(i + 1) for i in range(row)]
        line = ' '.join(numbers)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = reverse_number_triangle(5)
    print(result)