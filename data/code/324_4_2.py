import sys
def calculate_product(num1_str, num2_str):
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        return num1 * num2
    except ValueError:
        return None
if __name__ == '__main__':
    input1 = "10"
    input2 = "5"
    result = calculate_product(input1, input2)
    if result is not None:
        print(result)
    else:
        print("Error: Both inputs must be valid numbers.")