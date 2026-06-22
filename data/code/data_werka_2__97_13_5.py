def compute_and_table():
    operands = [True, False]
    table_rows = []
    for left in operands:
        for right in operands:
            result = left and right
            table_rows.append((left, right, result))
    return table_rows

if __name__ == '__main__':
    data = compute_and_table()
    for row in data:
        print(row)