def generate_star_grid(size=8):
    grid = []
    for i in range(size):
        row = '*' * size
        grid.append(row)
    return '\n'.join(grid)

if __name__ == '__main__':
    print(generate_star_grid())
    print(generate_star_grid(3))