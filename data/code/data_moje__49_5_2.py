def generate_square(rows, cols):
    return [('*' * cols) for _ in range(rows)]

if __name__ == '__main__':
    result = generate_square(8, 8)
    for row in result:
        print(row)