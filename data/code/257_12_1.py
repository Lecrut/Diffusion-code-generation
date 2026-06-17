import sys
def calculate_difference(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1
if __name__ == '__main__':
    sample_num1 = 25
    sample_num2 = 10
    try:
        n1 = int(sample_num1)
        n2 = int(sample_num2)
        difference = calculate_difference(n1, n2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please enter integer values.")