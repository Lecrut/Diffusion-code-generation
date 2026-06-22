def generate_star_square(size=3):
    return ('*' * size for _ in range(size))

if __name__ == '__main__':
    gen = generate_star_square()
    for row in gen:
        print(row)