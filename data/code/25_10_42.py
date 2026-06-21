def validate_input(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be an integer or a float")

def is_zero(x):
    validate_input(x)
    return x == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, 0.0, -0.0]
    results = {x: is_zero(x) for x in sample_values}
    print(results)