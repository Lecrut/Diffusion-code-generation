def create_grid(symbol, width, height):
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character.")
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer.")

    row = symbol * (width + 1)
    grid = [row]
    for _ in range(height - 2):
        grid.append("|" + " " * width + "|")
    if height > 1:
        grid.append(row)

    return "\n".join(grid)

if __name__ == '__main__':
    symbol = "+"
    width = 10
    height = 10
    result = create_grid(symbol, width, height)
    print(result)