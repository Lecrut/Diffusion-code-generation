def validate_inputs(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")

def add_two_integers(a: int, b: int) -> int:
    validate_inputs(a, b)
    return a + b

if __name__ == '__main__':
    result = add_two_integers(3, 5)
    print(result)