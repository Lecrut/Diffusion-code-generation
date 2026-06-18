def calculate_product(a: int, b: int) -> float:
    try:
        return a * b
    except TypeError as e:
        raise ValueError(f"Both inputs must be integers.") from e
if __name__ == '__main__':
    num1 = 42
    num2 = -73.5
    if not isinstance(num1, int) or not isinstance(num2, int):
        print("Error: Inputs must be integers")
    else:
        try:
            result = calculate_product(num1, num2)
            print(f"Product of {num1} and {num2}: {result}")
        except ValueError as ve:
            print(ve)