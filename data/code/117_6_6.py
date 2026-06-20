def validate_inputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers")

def calculate_difference(x, y):
    return x - y

if __name__ == '__main__':
    a = 10
    b = 5
    validate_inputs(a, b)
    result = calculate_difference(a, b)
    print(result)