def validate_integer(value: int) -> bool:
    return isinstance(value, int)

def add_integers(a: int, b: int) -> int:
    if not (validate_integer(a) and validate_integer(b)):
        raise ValueError("Both inputs must be integers.")
    return a + b

if __name__ == '__main__':
    num1 = 3
    num2 = 5
    result = add_integers(num1, num2)
    print(result)