def calculate_sum(num1, num2, num3):
    return num1 + num2 + num3
if __name__ == '__main__':
    try:
        number1 = 10
        number2 = 25
        number3 = 7
        result = calculate_sum(number1, number2, number3)
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")