def multiply_numbers(a: int, b: int) -> float:
    try:
        return a * b
    except TypeError as e:
        raise ValueError(f"Both operands must be integers.") from e
if __name__ == '__main__':
    num1 = 42
    num2 = -73.5
    if not isinstance(num1, int) or not isinstance(num2, int):
        print("Error: Both inputs must be integers.")
    else:
        result = multiply_numbers(num1, num2)
        print(f"Product of {num1} and {num2}: {result}")