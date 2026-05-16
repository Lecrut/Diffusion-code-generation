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
    input1 = "10.5"
    input2 = "10.5"
    compare_numbers(input1, input2)
    print("-" * 20)
    input1 = "5"
    input2 = "7"
    compare_numbers(input1, input2)
    print("-" * 20)
    input1 = "abc"
    input2 = "10"
    compare_numbers(input1, input2)