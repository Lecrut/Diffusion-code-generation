def validate_inputs(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

def add_two_numbers(x, y):
    validate_inputs(x, y)
    return x + y

if __name__ == '__main__':
    result = add_two_numbers(5, 3)
    print(result)