def validate_numbers(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both arguments must be numbers")

def add(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    try:
        print(add(15, 25))
    except ValueError as e:
        print(e)