def validate_inputs(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")

def generate_truth_table(a, b):
    validate_inputs(a, b)
    truth_table = {
        'A': [a, a],
        'B': [b, b],
        'AND': [a and b, a and b],
        'OR': [a or b, a or b],
        'NOT A': [not a, not a],
        'NOT B': [not b, not b]
    }
    return truth_table

if __name__ == '__main__':
    result = generate_truth_table(True, False)
    print(result)