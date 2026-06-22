def generate_star_square(size=6):
    row = '*' * size
    pattern = '\n'.join([row] * size)
    return pattern
if __name__ == '__main__':
    result = generate_star_square()
    print(result)