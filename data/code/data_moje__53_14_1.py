def reverse_number_triangle(n):
    result = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(i))
        result.append(' '.join(row))
    return '\n'.join(result)

if __name__ == '__main__':
    print(reverse_number_triangle(5))