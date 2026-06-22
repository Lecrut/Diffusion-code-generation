def validate_inputs(values):
    if not isinstance(values, list):
        raise ValueError("Inputs must be a list")
    for val in values:
        if not isinstance(val, bool):
            raise ValueError("All inputs must be boolean")
    if len(values) == 0:
        raise ValueError("Inputs list cannot be empty")
    return True

def compute_and_table(operands):
    validate_inputs(operands)
    table = []
    for op_a in operands:
        for op_b in operands:
            res = op_a and op_b
            table.append((op_a, op_b, res))
    return table

if __name__ == '__main__':
    sample_inputs = [True, False]
    result_rows = compute_and_table(sample_inputs)
    for row in result_rows:
        print(row)