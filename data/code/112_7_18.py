def add_values(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    return a + b

if __name__ == '__main__':
    num1 = 42
    num2 = 7
    result = add_values(num1, num2)
    print(result)