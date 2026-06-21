def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or a float")

def is_zero(x):
    validate_input(x)
    return x == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, None, '0', [], {}]
    results = {x: is_zero(x) if isinstance(x, (int, float)) else False for x in sample_values}
    print(results)