def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")

def add_numbers(a, b):
    validate_input(a)
    validate_input(b)
    return a + b

if __name__ == '__main__':
    result = add_numbers(3, 5)
    print(result)