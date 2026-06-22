def _validate_inputs(inputs):
    if not isinstance(inputs, (list, tuple)):
        raise ValueError("Inputs must be a list or tuple of strings")
    if len(inputs) == 0:
        raise ValueError("Inputs list cannot be empty")
    for item in inputs:
        if not isinstance(item, str):
            raise ValueError("Each input must be a string")
        if len(item) == 0:
            raise ValueError("Input strings cannot be empty")
    return list(inputs)

def _generate_combinations(n):
    combinations = []
    for i in range(1 << n):
        row = []
        for j in range(n):
            bit = (i >> (n - 1 - j)) & 1
            row.append(bool(bit))
        combinations.append(row)
    return combinations

def generate_truth_table(inputs):
    valid_inputs = _validate_inputs(inputs)
    n = len(valid_inputs)
    combinations = _generate_combinations(n)
    
    header = " | ".join(valid_inputs)
    separator = "-" * len(header)
    
    print(header)
    print(separator)
    
    for row in combinations:
        row_str = " | ".join(str(val) for val in row)
        print(row_str)

if __name__ == '__main__':
    inputs = ["X", "Y", "Z"]
    generate_truth_table(inputs)