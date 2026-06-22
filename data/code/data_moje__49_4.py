def generate_star_square(size=4):
    row = '*' * size
    return [row for _ in range(size)]
if __name__ == '__main__':
    star_square = generate_star_square()
    for row in star_square:
        print(row)