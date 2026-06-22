def generate_star_square(size):
    return ('* ' * size for _ in range(size))

if __name__ == '__main__':
    rows = generate_star_square(3)
    for row in rows:
        print(row)