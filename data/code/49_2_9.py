def generate_square(size):
    row = '*' * size
    return (row + '\n') * size

if __name__ == '__main__':
    size = 7
    result = generate_square(size)
    print(result, end='')