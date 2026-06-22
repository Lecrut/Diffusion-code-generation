def generate_star_grid(size=8):
    grid = ['*' * size for _ in range(size)]
    return '\n'.join(grid)

if __name__ == '__main__':
    print(generate_star_grid(5))