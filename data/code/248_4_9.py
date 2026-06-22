def validate_integers(a: int, b: int) -> None:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both parameters must be integers.")

def add(a: int, b: int) -> int:
    validate_integers(a, b)
    return a + b

if __name__ == '__main__':
    num1 = 3
    num2 = 5
    result = add(num1, num2)
    print(result)