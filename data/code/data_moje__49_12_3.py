def generate_star_grid(size=8):
    rows = []
    for _ in range(size):
        row = '*' * size
        rows.append(row)
    return '\n'.join(rows)

if __name__ == '__main__':
    grid_size = 5
    result = generate_star_grid(grid_size)
    print(result)