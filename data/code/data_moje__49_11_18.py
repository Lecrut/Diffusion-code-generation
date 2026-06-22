def generate_star_grid(rows: int, cols: int) -> str:
    grid_lines = ['*' * cols for _ in range(rows)]
    return '\n'.join(grid_lines)

if __name__ == '__main__':
    print(generate_star_grid(10, 10))