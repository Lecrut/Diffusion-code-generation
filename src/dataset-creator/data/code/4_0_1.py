import sys
def calculate_sum(num1, num2, num3):
    return num1 + num2 + num3
if __name__ == '__main__':
    sample_num1 = 10
    sample_num2 = 25
    sample_num3 = 5
    try:
        number1 = int(sample_num1)
        number2 = int(sample_num2)
        number3 = int(sample_num3)
        total_sum = calculate_sum(number1, number2, number3)
        print(total_sum)
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are integers.")