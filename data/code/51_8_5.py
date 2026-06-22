def generate_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

if __name__ == '__main__':
    generate_pyramid(5)