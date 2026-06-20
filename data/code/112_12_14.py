def validate_input(a: int, b: int) -> bool:
    return isinstance(a, int) and isinstance(b, int)

def add_integers(a: int, b: int) -> int:
    if not validate_input(a, b):
        raise ValueError("Both inputs must be integers.")
    return a + b

if __name__ == '__main__':
    result = add_integers(3, 5)
    print(result)