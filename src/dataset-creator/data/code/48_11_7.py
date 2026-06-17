def divide_numbers(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric.")
    try:
        a = int(a)
        b = int(b)
    except ValueError as e:
        raise TypeError(f"Arguments must be convertible to integers. Error details: {e}") from e
    if not isinstance(a, (int)) or not isinstance(b, (int)):
        raise TypeError("After conversion, arguments must remain integers.")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
if __name__ == '__main__':
    result = divide_numbers(10, 2)
    print(result)