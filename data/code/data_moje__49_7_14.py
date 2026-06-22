def generate_square(size):
    rows = ("*" * size for _ in range(size))
    for row in rows:
        print(row)

if __name__ == '__main__':
    generate_square(3)