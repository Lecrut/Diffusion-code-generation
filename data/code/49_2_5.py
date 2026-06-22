def generate_square(size=7):
    return ('\n'.join('*' * size for _ in range(size)))

if __name__ == '__main__':
    print(generate_square(7))