import sys
def compare_numbers(num1_str, num2_str):
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        if num1 == num2:
            print("The numbers are equal.")
        else:
            print("The numbers are not equal.")
    except ValueError:
        print("Error: Invalid input. Please enter valid numeric values.")
if __name__ == '__main__':
    num1_str = "10.5"
    num2_str = "10.5"
    compare_numbers(num1_str, num2_str)
    print("-" * 20)
    num1_str = "5"
    num2_str = "6"
    compare_numbers(num1_str, num2_str)
    print("-" * 20)
    num1_str = "abc"
    num2_str = "10"
    compare_numbers(num1_str, num2_str)