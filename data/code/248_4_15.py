def validate_input(a: int, b: int) -> None:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative")

def add(a: int, b: int) -> int:
    validate_input(a, b)
    return a + b

if __name__ == '__main__':
    result = add(3, 5)
    print(result)