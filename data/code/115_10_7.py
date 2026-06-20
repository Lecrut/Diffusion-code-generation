def safe_divide(dividend, divisor):
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise ValueError("Both operands must be numbers.")
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend / divisor

if __name__ == '__main__':
    try:
        result = safe_divide(20.5, 4.2)
    except Exception as e:
        print(e)
    else:
        print(result)