def validate_input(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return True

def add_integers(a: int, b: int) -> int:
    if validate_input(a, b):
        return a + b

if __name__ == '__main__':
    result = add_integers(3, 5)
    print(result)