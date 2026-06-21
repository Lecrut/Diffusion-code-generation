OPERATORS = [True, False]

def compute_and_table():
    table_rows = []
    for operand_first in OPERATORS:
        for operand_second in OPERATORS:
            output_value = operand_first and operand_second
            table_rows.append((operand_first, operand_second, output_value))
    return table_rows

if __name__ == '__main__':
    computed_table = compute_and_table()
    for row in computed_table:
        print(row)