def compute_xor_table():
    values = (0, 1)
    rows = []
    for first in values:
        for second in values:
            difference = first ^ second
            rows.append((first, second, difference))
    return rows

if __name__ == '__main__':
    data = compute_xor_table()
    for entry in data:
        print(entry)