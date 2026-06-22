def create_grid(symbol):
    rows = [symbol * 10 for _ in range(10)]
    grid = "\n".join(rows)
    return grid

if __name__ == '__main__':
    symbol_val = "+"
    result = create_grid(symbol_val)
    print(result)