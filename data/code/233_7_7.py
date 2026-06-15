def fill_rectangle(rows, symbol):
    if not rows:
        return []
    num_rows = len(rows)
    num_cols = len(rows[0])
    filled = []
    for i in range(num_rows):
        row_str = ""
        for j in range(num_cols):
            if rows[i][j] == '*':
                row_str += symbol
            else:
                row_str += rows[i][j]
        filled.append(row_str)
    return filled
if __name__ == '__main__':
    sample_rows = [
        "***",
        "*.*",
        "***"
    ]
    symbol_to_fill = "#"
    result = fill_rectangle(sample_rows, symbol_to_fill)
    print(result)