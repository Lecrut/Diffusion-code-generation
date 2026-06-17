import sys
def calculate_product(num1, num2):
    return num1 * num2
if __name__ == '__main__':
    try:
        input_str1 = "10"
        input_str2 = "5"
        num1 = float(input_str1)
        num2 = float(input_str2)
        result = calculate_product(num1, num2)
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")