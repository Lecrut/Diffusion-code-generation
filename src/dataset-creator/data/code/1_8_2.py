import sys
def calculate_difference(num1, num2):
    if isinstance(num1, float) or isinstance(num2, float):
        result = num1 - num2
        print(f"{result:.2f}")
    else:
        result = num1 - num2
        print(result)
if __name__ == '__main__':
    input_data = [3.14159, 2.71828]
    num1 = input_data[0]
    num2 = input_data[1]
    calculate_difference(num1, num2)