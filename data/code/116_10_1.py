import sys
def calculate_sum(num1, num2, num3):
    return num1 + num2 + num3
if __name__ == '__main__':
    number1 = 10
    number2 = 25
    number3 = 5
    try:
        sum_result = calculate_sum(number1, number2, number3)
        print(sum_result)
    except TypeError:
        print("Error: One or more inputs were not valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")