def validate_integers(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both parameters must be integers.")
    return True

def add(a: int, b: int) -> int:
    if not validate_integers(a, b):
        return None
    return a + b

if __name__ == '__main__':
    num1 = 3
    num2 = 5
    result = add(num1, num2)
    print(result)