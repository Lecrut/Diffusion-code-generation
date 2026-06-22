def calculate_sum(num1: int, num2: int) -> int:
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers")
    return num1 + num2

if __name__ == '__main__':
    try:
        number1 = 15
        number2 = 27
        result = calculate_sum(number1, number2)
        print(result)
    except ValueError as e:
        print(e)