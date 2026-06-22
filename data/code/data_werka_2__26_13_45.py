def validate_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")

def is_greater_than(a, b):
    validate_integers(a, b)
    return a > b

if __name__ == '__main__':
    try:
        result = is_greater_than(25, 20)
        print(result)
    except ValueError as e:
        print(e)