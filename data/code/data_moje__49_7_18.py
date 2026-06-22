def generate_square_of_stars():
    size = 3
    return '\n'.join(''.join('*' for _ in range(size)) for _ in range(size))

if __name__ == '__main__':
    print(generate_square_of_stars())