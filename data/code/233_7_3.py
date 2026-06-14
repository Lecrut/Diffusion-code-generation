def fill_rectangle(rows, symbol):
    if not rows:
        return []
    num_rows = len(rows)
    if num_rows == 0:
        return []
    num_cols = len(rows[0])
    result = []
    for i in range(num_rows):
        new_row = []
        for j in range(num_cols):
            if rows[i][j] == '*':
                new_row.append(symbol)
            else:
                new_row.append(rows[i][j])
        result.append("".join(new_row))
    return result
if __name__ == '__main__':
    sample_rows = [
        "***",
        "*.*",
        "***"
    ]
    symbol_to_fill = "#"
    filled_rectangle = fill_rectangle(sample_rows, symbol_to_fill)
    print(filled_rectangle)
    sample_rows_2 = [
        "*****",
        "*.*.*",
        "*****",
        "*.*.*"
    ]
    symbol_to_fill_2 = "X"
    filled_rectangle_2 = fill_rectangle(sample_rows_2, symbol_to_fill_2)
    print(filled_rectangle_2)
    sample_rows_3 = [
        "abc",
        "def",
        "ghi"
    ]
    symbol_to_fill_3 = "0"
    filled_rectangle_3 = fill_rectangle(sample_rows_3, symbol_to_fill_3)
    print(filled_rectangle_3)