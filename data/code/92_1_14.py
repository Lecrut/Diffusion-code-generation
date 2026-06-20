def validate_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")

def find_opposite_truth(truth):
    validate_input(truth)
    return not truth

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        result = find_opposite_truth(value)
        print(f"Opposite of {value} is {result}")