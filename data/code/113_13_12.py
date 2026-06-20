def validate_integers(a: int, b: int) -> None:
    if not isinstance(a, int):
        raise ValueError("First input must be an integer")
    if not isinstance(b, int):
        raise ValueError("Second input must be an integer")

def subtract_integers(a: int, b: int) -> int:
    validate_integers(a, b)
    return a - b

if __name__ == '__main__':
    num1 = 20
    num2 = 7
    result = subtract_integers(num1, num2)
    print(result)