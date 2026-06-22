def validate_input(a: int, b: int) -> None:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")

def add_numbers(a: int, b: int) -> int:
    validate_input(a, b)
    return a + b

if __name__ == '__main__':
    num1 = 15
    num2 = 27
    result = add_numbers(num1, num2)
    print(result)