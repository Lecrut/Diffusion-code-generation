def generate_hollow_square(size):
    return '\n'.join('*' if i == 0 or i == size - 1 or j == 0 or j == size - 1 else ' ' for i in range(size) for j in range(size))

if __name__ == '__main__':
    print(generate_hollow_square(7))