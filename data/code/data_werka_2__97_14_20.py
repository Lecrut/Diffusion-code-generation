OR_OPERANDS = [True, False]

def compute_or_truth_table():
    operand_list = OR_OPERANDS
    result_rows = []
    for first_val in operand_list:
        for second_val in operand_list:
            row_data = {
                "x": first_val,
                "y": second_val,
                "x | y": first_val or second_val
            }
            result_rows.append(row_data)
    return result_rows

if __name__ == '__main__':
    computed_table = compute_or_truth_table()
    print(computed_table)