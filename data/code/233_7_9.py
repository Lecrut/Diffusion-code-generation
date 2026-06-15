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
        "*****",
        "*    ",
        "*****"
    ]
    sample_symbol = "#"
    filled = fill_rectangle(sample_rows, sample_symbol)
    print(filled)