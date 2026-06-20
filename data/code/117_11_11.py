def validate_inputs(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

def calculate_difference(a, b):
    validate_inputs(a, b)
    return abs(a - b)

if __name__ == '__main__':
    num1 = 1000000000000000000
    num2 = 500000000000000000
    result = calculate_difference(num1, num2)
    print(result)