def validate_arguments(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")

def sum_two_numbers(a, b):
    validate_arguments(a, b)
    return a + b

if __name__ == '__main__':
    result = sum_two_numbers(5, 3)
    print(result)