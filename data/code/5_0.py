import sys
def calculate_difference(length1, length2):
    try:
        num1 = float(length1)
        num2 = float(length2)
        return num1 - num2
    except ValueError:
        return "Error: Both inputs must be valid numbers."
if __name__ == '__main__':
    input_length1 = "15.5"
    input_length2 = "8.2"
    result = calculate_difference(input_length1, input_length2)
    print(result)