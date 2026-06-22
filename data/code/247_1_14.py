def validate_integers(a: int, b: int) -> bool:
    return isinstance(a, int) and isinstance(b, int)

def add_numbers(a: int, b: int) -> int:
    if not validate_integers(a, b):
        raise ValueError("Both inputs must be integers.")
    return a + b

if __name__ == '__main__':
    result1 = add_numbers(5, 3)
    print(result1)
    result2 = add_numbers(-10, 20)
    print(result2)