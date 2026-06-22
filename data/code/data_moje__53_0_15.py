def generate_reverse_triangle(rows):
    return [' ' * i + str(j) * (rows * 2 - 1 - 2 * i) for i in range(rows) for j in [1]]

if __name__ == '__main__':
    print(generate_reverse_triangle(5))