import sys
def calculate_product(num1, num2):
    return num1 * num2
if __name__ == '__main__':
    try:
        num1_str = "15"
        num2_str = "7"
        num1 = float(num1_str)
        num2 = float(num2_str)
        result = calculate_product(num1, num2)
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")