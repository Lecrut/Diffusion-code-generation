def generate_star_square(size):
    rows = ( '*' * size for _ in range(size) )
    return '\n'.join(rows)

if __name__ == '__main__':
    size = 3
    result = generate_star_square(size)
    print(result)