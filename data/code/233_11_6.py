def create_symbol_grid(width, height, symbol):
    return '\n'.join([symbol * width for _ in range(height)])

if __name__ == '__main__':
    grid = create_symbol_grid(5, 4, '*')
    print(grid)