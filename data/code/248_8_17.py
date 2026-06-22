def validate_integers(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return True

def add_two_integers(a: int, b: int) -> int:
    if validate_integers(a, b):
        return a + b
    else:
        raise ValueError("Invalid input types.")

if __name__ == '__main__':
    result = add_two_integers(3, 5)
    print(result)