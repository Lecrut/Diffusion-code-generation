import sys
def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    sample_num1 = 45
    sample_num2 = 18
    try:
        num1 = int(sample_num1)
        num2 = int(sample_num2)
        difference = calculate_difference(num1, num2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")