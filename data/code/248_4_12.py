def validate_int(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")

def add(a: int, b: int) -> int:
    validate_int(a)
    validate_int(b)
    return a + b

if __name__ == '__main__':
    result = add(3, 5)
    print(result)