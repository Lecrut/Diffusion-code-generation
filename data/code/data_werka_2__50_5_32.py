def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Inputs must be numbers")

def non_negative_difference(a, b):
    validate_input(a)
    validate_input(b)
    return max(a - b, b - a)

if __name__ == '__main__':
    sample_values = [5, 10]
    print(non_negative_difference(sample_values[0], sample_values[1]))