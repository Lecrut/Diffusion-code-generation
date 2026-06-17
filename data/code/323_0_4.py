import sys
def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    sample_num1 = 50
    sample_num2 = 25
    try:
        num1 = float(sample_num1)
        num2 = float(sample_num2)
        difference = calculate_difference(num1, num2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")