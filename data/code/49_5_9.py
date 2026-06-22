def generate_square_star_pattern(dimensions):
    rows = ['*' * dimensions for _ in range(dimensions)]
    return '\n'.join(rows)

if __name__ == '__main__':
    dimension = 8
    result = generate_square_star_pattern(dimension)
    print(result)