def validate_inputs(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return True

def sum_two_numbers(a, b):
    validate_inputs(a, b)
    return a + b

if __name__ == '__main__':
    result = sum_two_numbers(3, 5)
    print(result)