def fill_rectangle(rows, symbol):
    if not rows:
        return []
    num_rows = len(rows)
    if num_rows == 0:
        return []
    num_cols = len(rows[0])
    result = []
    for row in rows:
        filled_row = "".join([symbol if char != ' ' else char for char in row])
        result.append(filled_row)
    return result
if __name__ == '__main__':
    sample_rows = [
        "*****  ",
        " *   * ",
        "*****  ",
        " *   * "
    ]
    symbol = "*"
    filled = fill_rectangle(sample_rows, symbol)
    print(filled)