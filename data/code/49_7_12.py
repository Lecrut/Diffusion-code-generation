def generate_star_square():
    return '\n'.join(''.join('*' for _ in range(3)) for _ in range(3))

if __name__ == '__main__':
    print(generate_star_square())