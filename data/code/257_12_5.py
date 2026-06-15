import sys
def calculate_difference(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    try:
        n1 = int(num1)
        n2 = int(num2)
        difference = calculate_difference(n1, n2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please enter integer values.")