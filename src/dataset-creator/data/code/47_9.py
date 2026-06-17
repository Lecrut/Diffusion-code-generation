def calculate_product(a: int, b: int) -> float:
    try:
        return a * b
    except TypeError as e:
        raise ValueError(f"Both operands must be integers.") from e
if __name__ == '__main__':
    num1 = 42
    num2 = -73
    result = calculate_product(num1, num2)
    print(result)