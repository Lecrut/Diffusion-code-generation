def generate_star_square(size):
    rows = ((('*' * size) for _ in range(size)) for _ in range(size))
    return '\n'.join(''.join(row) for row in rows)

if __name__ == '__main__':
    print(generate_star_square(3))