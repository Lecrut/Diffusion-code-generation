def multiply_numbers(a: int, b: int) -> float:
    try:
        return a * b
    except TypeError as e:
        print(f"Error: Invalid input types. {e}")
        raise ValueError("Both operands must be integers.") from e
if __name__ == '__main__':
    num1 = 42
    num2 = -73
    try:
        result = multiply_numbers(num1, num2)
        print(f"Product of {num1} and {num2}: {result}")
    except ValueError as ve:
        print(ve)