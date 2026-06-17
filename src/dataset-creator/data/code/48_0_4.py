def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
if __name__ == '__main__':
    num1 = 25.0
    num2 = 4.0
    try:
        result = divide_numbers(num1, num2)
        print(f"{num1} divided by {num2} equals {result}")
    except ValueError as e:
        print(e)