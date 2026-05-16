import sys
def calculate_difference(len1, len2):
    try:
        num1 = float(len1)
        num2 = float(len2)
        return num1 - num2
    except ValueError:
        return "Error: Both inputs must be valid numbers."
if __name__ == '__main__':
    input_length1 = "15.5"
    input_length2 = "7.2"
    result = calculate_difference(input_length1, input_length2)
    print(result)