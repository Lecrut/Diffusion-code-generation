def divide_numbers(num1: float, num2: float) -> float:
    return num1 / num2 if num2 != 0 else float('inf')

if __name__ == '__main__':
    result = divide_numbers(10.0, 2.0)
    print(result)
    result = divide_numbers(5.0, 0.0)
    print(result)