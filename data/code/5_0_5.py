import sys
def calculate_difference(len1, len2):
    try:
        num1 = float(len1)
        num2 = float(len2)
        return num1 - num2
    except ValueError:
        return "Error: Invalid input. Please provide numeric values."
if __name__ == '__main__':
    input1 = "15.5"
    input2 = "8.2"
    result = calculate_difference(input1, input2)
    print(result)