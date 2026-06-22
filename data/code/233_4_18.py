def generate_grid(symbol):
    row = symbol * 10 + "\n"
    return row * 10

if __name__ == '__main__':
    grid_symbol = "+"
    grid_result = generate_grid(grid_symbol)
    print(grid_result)