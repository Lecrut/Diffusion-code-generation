def validate_integers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")

def add_two_integers(a: int, b: int) -> int:
    validate_integers(a, b)
    return a + b

if __name__ == '__main__':
    result = add_two_integers(3, 5)
    print(result)