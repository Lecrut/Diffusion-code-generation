def reverse_number_triangle(size):
    if size <= 0:
        return []
    return [
        ''.join(str(size - row + col) for col in range(row + 1))
        for row in range(size)
    ]

if __name__ == '__main__':
    result = reverse_number_triangle(5)
    for line in result:
        print(line)