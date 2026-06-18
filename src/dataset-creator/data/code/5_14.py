import sys
def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    try:
        input1_str = "15"
        input2_str = "7"
        num1 = float(input1_str)
        num2 = float(input2_str)
        result = calculate_difference(num1, num2)
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")