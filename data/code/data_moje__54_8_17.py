def generate_hollow_square(size):
    return [print(*['*' if r == 0 or r == size - 1 or c == 0 or c == size - 1 else ' ' for c in range(size)], sep='') for r in range(size)]

if __name__ == '__main__':
    generate_hollow_square(7)