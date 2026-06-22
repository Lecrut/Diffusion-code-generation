def generate_and_truth_table(inputs=None):
    if inputs is None:
        inputs = [True, False]
    if not isinstance(inputs, list):
        raise ValueError("Inputs must be a list")
    if len(inputs) == 0:
        return []
    for val in inputs:
        if not isinstance(val, bool):
            raise ValueError("All inputs must be boolean values")
    rows = []
    for first in inputs:
        for second in inputs:
            result = first and second
            rows.append((first, second, result))
    return rows

if __name__ == '__main__':
    sample_values = [True, False]
    truth_data = generate_and_truth_table(sample_values)
    for row in truth_data:
        print(row)