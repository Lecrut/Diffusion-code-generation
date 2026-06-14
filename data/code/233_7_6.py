def fill_rectangle(rows, symbol):
    if not rows:
        return []
    num_rows = len(rows)
    if num_rows == 0:
        return []
    num_cols = len(rows[0])
    filled_rectangle = []
    for row in rows:
        filled_row = "".join([symbol if char != ' ' else ' ' for char in row])
        filled_rectangle.append(filled_row)
    return filled_rectangle
if __name__ == '__main__':
    sample_rows = [
        "*****  ",
        " *   * ",
        "*****  "
    ]
    symbol = "*"
    result = fill_rectangle(sample_rows, symbol)
    print(result)