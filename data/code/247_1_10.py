def validate_inputs(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return True

def add_numbers(a: int, b: int) -> int:
    if not validate_inputs(a, b):
        return None
    return a + b

if __name__ == '__main__':
    result1 = add_numbers(5, 3)
    print(result1)
    result2 = add_numbers(-10, 20)
    print(result2)