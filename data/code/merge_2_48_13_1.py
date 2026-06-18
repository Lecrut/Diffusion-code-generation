def divide_numbers(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numeric types.")
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValueError("Operands cannot be converted to valid numbers.")
    if b == 0.0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
if __name__ == '__main__':
    result = divide_numbers(10, 2)
    print(result)