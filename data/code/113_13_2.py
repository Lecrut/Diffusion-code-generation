def subtract_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a - b

if __name__ == '__main__':
    num1 = 20
    num2 = 7
    result = subtract_integers(num1, num2)
    print(result)