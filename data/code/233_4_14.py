def create_grid(symbol):
    rows = [symbol * 10 for _ in range(10)]
    return "\n".join(rows)

if __name__ == '__main__':
    symbol = "+"
    result = create_grid(symbol)
    print(result)