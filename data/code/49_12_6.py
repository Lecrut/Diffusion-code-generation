def star_square(size=8):
    return '\n'.join('*' * size for _ in range(size))

if __name__ == '__main__':
    print(star_square())
    print(star_square(5))