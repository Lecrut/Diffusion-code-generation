from itertools import product

def generate_logical_or_table():
    values = [True, False]
    combinations = product(values, repeat=2)
    rows = []
    for first, second in combinations:
        row = {"left_operand": first, "right_operand": second, "outcome": first or second}
        rows.append(row)
    return rows

if __name__ == '__main__':
    table_data = generate_logical_or_table()
    print(table_data)