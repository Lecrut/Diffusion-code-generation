def compute_xor_table():
    inputs = (0, 1)
    rows = []
    for first in inputs:
        for second in inputs:
            if first == second:
                rows.append((first, second, 0))
            else:
                rows.append((first, second, 1))
    return rows

if __name__ == '__main__':
    table_data = compute_xor_table()
    for entry in table_data:
        print(entry)