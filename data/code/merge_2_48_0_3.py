def divide_numbers(a: float, b: float) -> str:
    if b == 0:
        return "Error: Division by zero"
    result = a / b
    try:
        int_result = int(result)
        return f"{int_result}"
    except (OverflowError, ValueError):
        return f"{result:.6f}"
if __name__ == '__main__':
    num1 = 42.5
    num2 = 7
    output = divide_numbers(num1, num2)
    print(output)