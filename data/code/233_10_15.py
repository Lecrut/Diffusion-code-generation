def fill_rectangle(width, height, symbol):
    if not all(isinstance(i, int) and i > 0 for i in (width, height)):
        raise ValueError("Width and height must be positive integers.")
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character.")

    return '\n'.join([symbol * width for _ in range(height)])

if __name__ == '__main__':
    width = 10
    height = 5
    symbol = "*"
    print(fill_rectangle(width, height, symbol))