def generate_and_truth_table():
    operands = [True, False]
    output_rows = []
    for first_operand in operands:
        for second_operand in operands:
            logical_result = first_operand and second_operand
            output_rows.append((first_operand, second_operand, logical_result))
    return output_rows

if __name__ == '__main__':
    sample_data = generate_and_truth_table()
    for current_row in sample_data:
        print(current_row)