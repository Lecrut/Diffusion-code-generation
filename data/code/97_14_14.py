def validate_inputs(values):
    if not isinstance(values, list):
        raise ValueError("Inputs must be a list")
    for val in values:
        if not isinstance(val, bool):
            raise ValueError("All inputs must be boolean")

def compute_or_table(inputs):
    validate_inputs(inputs)
    rows = []
    for i in inputs:
        for j in inputs:
            row = {
                "first": i,
                "second": j,
                "outcome": i or j
            }
            rows.append(row)
    return rows

if __name__ == '__main__':
    sample_values = [True, False]
    output = compute_or_table(sample_values)
    print(output)