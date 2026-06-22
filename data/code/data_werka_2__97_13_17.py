TRUE_VALUE = True
FALSE_VALUE = False
OPERANDS = [TRUE_VALUE, FALSE_VALUE]

def compute_and_operation(left, right):
    return left and right

def generate_and_truth_table():
    table_rows = []
    for operand_a in OPERANDS:
        for operand_b in OPERANDS:
            computed_result = compute_and_operation(operand_a, operand_b)
            table_rows.append((operand_a, operand_b, computed_result))
    return table_rows

if __name__ == '__main__':
    truth_table_data = generate_and_truth_table()
    for row in truth_table_data:
        print(row)