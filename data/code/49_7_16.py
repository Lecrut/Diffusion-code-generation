def generate_star_square(size):
    return '\n'.join(''.join('*' for _ in range(size)) for _ in range(size))

if __name__ == '__main__':
    result = generate_star_square(3)
    print(result)