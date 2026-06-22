TRUE_VAL = True
FALSE_VAL = False
OPERANDS = [TRUE_VAL, FALSE_VAL]

def validate_inputs(values):
    if not isinstance(values, list):
        raise ValueError("Inputs must be a list")
    if len(values) == 0:
        raise ValueError("Inputs list cannot be empty")
    for val in values:
        if not isinstance(val, bool):
            raise ValueError("All inputs must be boolean")
    return True

def compute_and_operation(a, b):
    return a and b

def generate_truth_table(operands):
    validate_inputs(operands)
    table = []
    for a in operands:
        for b in operands:
            result = compute_and_operation(a, b)
            table.append((a, b, result))
    return table

if __name__ == '__main__':
    sample_inputs = OPERANDS
    truth_table = generate_truth_table(sample_inputs)
    for row in truth_table:
        print(row)