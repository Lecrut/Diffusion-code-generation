INPUT_DOMAIN = (0, 1)

def compute_xor_table():
    rows = []
    for first in INPUT_DOMAIN:
        for second in INPUT_DOMAIN:
            value = first ^ second
            rows.append((first, second, value))
    return rows

if __name__ == '__main__':
    table_data = compute_xor_table()
    for entry in table_data:
        print(entry)