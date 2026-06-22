def reverse_number_triangle(rows=5):
    result = []
    for i in range(rows, 0, -1):
        line = ' '.join(str(n) for n in range(1, i + 1))
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(reverse_number_triangle(5))