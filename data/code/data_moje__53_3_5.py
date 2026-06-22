def reverse_number_triangle(n):
    result = []
    for i in range(n, 0, -1):
        result.append(str(i) * i)
    return '\n'.join(result)

if __name__ == '__main__':
    rows = 5
    print(reverse_number_triangle(rows))