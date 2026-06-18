def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is undefined.")
    return a / b
if __name__ == '__main__':
    num1 = 25.5
    num2 = 4
    result = divide_numbers(num1, num2)
    print(result)