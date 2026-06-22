def build_and_table(operands):
    if not operands:
        return []
    return [[a, b, a and b] for a in operands for b in operands]

if __name__ == '__main__':
    values = [True, False]
    table_rows = build_and_table(values)
    for row in table_rows:
        print(row)