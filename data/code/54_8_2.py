def generate_hollow_square(size):
    return '\n'.join('*' * size if i in (0, size - 1) else '*' + ' ' * (size - 2) + '*' for i in range(size))

if __name__ == '__main__':
    result = generate_hollow_square(7)
    print(result)