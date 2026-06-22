def generate_hollow_square(size):
    return '\n'.join([''.join(['*' if i == 0 or i == size - 1 or j == 0 or j == size - 1 else ' ' for j in range(size)]) for i in range(size)])

if __name__ == '__main__':
    square_size = 7
    print(generate_hollow_square(square_size))