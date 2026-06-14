def fill_rectangle(rows, symbol):
    if not rows:
        return []
    num_rows = len(rows)
    num_cols = len(rows[0])
    filled_rectangle = []
    for row in rows:
        new_row = ""
        for char in row:
            if char == '*':
                new_row += symbol
            else:
                new_row += char
        filled_rectangle.append(new_row)
    return filled_rectangle
if __name__ == '__main__':
    sample_rows = [
        "*****"
    ]
    symbol = "#"
    result1 = fill_rectangle(sample_rows, symbol)
    print(f"Input rows: {sample_rows}")
    print(f"Symbol: {symbol}")
    print(f"Result: {result1}")
    sample_rows2 = [
        "*****",
        "*****"
    ]
    symbol2 = "@"
    result2 = fill_rectangle(sample_rows2, symbol2)
    print(f"\nInput rows: {sample_rows2}")
    print(f"Symbol: {symbol2}")
    print(f"Result: {result2}")
    sample_rows3 = [
        "abcde",
        "fghij"
    ]
    symbol3 = "X"
    result3 = fill_rectangle(sample_rows3, symbol3)
    print(f"\nInput rows: {sample_rows3}")
    print(f"Symbol: {symbol3}")
    print(f"Result: {result3}")