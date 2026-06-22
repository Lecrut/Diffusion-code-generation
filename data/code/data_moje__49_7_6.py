def generate_square_of_stars(size):
    def create_row(r):
        return '*' * size
    return (create_row(r) for r in range(size))

if __name__ == '__main__':
    result = list(generate_square_of_stars(3))
    for row in result:
        print(row)