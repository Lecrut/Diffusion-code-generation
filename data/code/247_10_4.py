def validate_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

def sum_two_integers(a, b):
    validate_integers(a, b)
    return a + b

if __name__ == '__main__':
    result = sum_two_integers(3, 5)
    print(result)