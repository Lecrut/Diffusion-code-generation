def _validate_boolean(input_list):
    if not isinstance(input_list, (list, tuple)):
        raise TypeError("Inputs must be a list or tuple.")
    for index, value in enumerate(input_list):
        if not isinstance(value, bool):
            raise ValueError(f"Element at index {index} is not a boolean.")
    return input_list

def compute_logical_and_table(operands):
    validated_operands = _validate_boolean(operands)
    table = []
    for first_operand in validated_operands:
        for second_operand in validated_operands:
            computed_result = first_operand and second_operand
            table.append((first_operand, second_operand, computed_result))
    return table

if __name__ == '__main__':
    sample_inputs = [True, False]
    generated_table = compute_logical_and_table(sample_inputs)
    for row in generated_table:
        print(row)