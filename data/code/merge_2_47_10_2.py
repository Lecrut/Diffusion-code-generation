def multiply_numbers(a: int | float, b: int | float) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric.")
    result = a * b
    print(f"{a} multiplied by {b} equals {result}")
if __name__ == '__main__':
    multiply_numbers(0, -5)