TRUE_INPUT = True
FALSE_INPUT = False
OPERANDS = (TRUE_INPUT, FALSE_INPUT)

def calculate_and_operation(left_val, right_val):
    return left_val and right_val

def generate_truth_table(operand_list):
    table_output = []
    for first_operand in operand_list:
        for second_operand in operand_list:
            computed_result = calculate_and_operation(first_operand, second_operand)
            table_output.append((first_operand, second_operand, computed_result))
    return table_output

if __name__ == '__main__':
    generated_table = generate_truth_table(OPERANDS)
    for row in generated_table:
        print(row)