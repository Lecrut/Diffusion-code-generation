def generate_reverse_triangle(rows):
    return [' ' * i + str(rows - i) * (2 * (rows - i) - 1) for i in range(rows)]

if __name__ == '__main__':
    result = generate_reverse_triangle(5)
    for line in result:
        print(line)