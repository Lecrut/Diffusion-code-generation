def generate_reverse_triangle(rows):
    return [' '.join(str(rows - row - col + 1) for col in range(rows - row)) for row in range(rows)]

if __name__ == '__main__':
    result = generate_reverse_triangle(5)
    for row in result:
        print(row)