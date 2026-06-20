def calculate_sum(num1, num2, num3):
    if not all(isinstance(i, (int, float)) for i in [num1, num2, num3]):
        raise ValueError("All inputs must be numbers")
    return num1 + num2 + num3

if __name__ == '__main__':
    number1 = 10
    number2 = 25
    number3 = 5
    try:
        sum_result = calculate_sum(number1, number2, number3)
        print(sum_result)
    except ValueError as e:
        print(e)