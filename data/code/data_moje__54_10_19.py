def generate_hollow_square(size):
    return [
        ('*' if (row == 0 or row == size - 1 or col == 0 or col == size - 1) else ' ') * size + ('' if size == 1 else '')
        for row in range(size)
    ] if size > 0 else []

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)