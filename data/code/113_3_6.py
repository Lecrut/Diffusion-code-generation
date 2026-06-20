def validate_input(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return True

def subtract_numbers(a, b):
    if validate_input(a, b):
        return a - b

if __name__ == '__main__':
    result = subtract_numbers(5, 3)
    print(result)