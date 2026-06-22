def validate_inputs(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

def calculate_sum(a, b):
    validate_inputs(a, b)
    return a + b

if __name__ == '__main__':
    result = calculate_sum(15, 27)
    print(result)