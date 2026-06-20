def validate_numbers(a: int, b: int) -> None:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

def add_numbers(num1: int, num2: int) -> int:
    validate_numbers(num1, num2)
    return num1 + num2

if __name__ == '__main__':
    result = add_numbers(10, 5)
    print(result)