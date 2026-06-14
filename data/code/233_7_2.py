def fill_rectangle(rows, symbol):
    if not rows:
        return []
    num_rows = len(rows)
    result = []
    for row in rows:
        filled_row = ""
        for char in row:
            if char == '*':
                filled_row += symbol
            else:
                filled_row += char
        result.append(filled_row)
    return result
if __name__ == '__main__':
    sample_rows = [
        "*****"
    ]
    symbol_to_fill = "#"
    filled_rectangle = fill_rectangle(sample_rows, symbol_to_fill)
    print(filled_rectangle)
    sample_rows_2 = [
        "***--",
        "--**-"
    ]
    symbol_to_fill_2 = "X"
    filled_rectangle_2 = fill_rectangle(sample_rows_2, symbol_to_fill_2)
    print(filled_rectangle_2)
    sample_rows_3 = [
        "abcde",
        "fghij",
        "klmno"
    ]
    symbol_to_fill_3 = "@"
    filled_rectangle_3 = fill_rectangle(sample_rows_3, symbol_to_fill_3)
    print(filled_rectangle_3)