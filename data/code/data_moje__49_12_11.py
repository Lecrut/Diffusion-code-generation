def generate_star_grid(size=8):
    line = '*' * size
    return '\n'.join([line] * size)

if __name__ == '__main__':
    result = generate_star_grid(8)
    print(result)