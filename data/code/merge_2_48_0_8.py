def divide_numbers(a: float, b: float) -> float:
    if abs(b) < 1e-9:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
if __name__ == '__main__':
    num1 = 20.5
    num2 = 4
    result = divide_numbers(num1, num2)
    print(result)