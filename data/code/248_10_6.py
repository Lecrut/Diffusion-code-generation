def add_numbers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    return a + b

if __name__ == '__main__':
    num1 = 15
    num2 = 27
    result = add_numbers(num1, num2)
    print(result)