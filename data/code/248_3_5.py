def validate_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a, b

def sum_two_numbers(a, b):
    a, b = validate_integers(a, b)
    return a + b

if __name__ == '__main__':
    result1 = sum_two_numbers(3, 5)
    print(result1)
    result2 = sum_two_numbers(7, 9)
    print(result2)