import sys
def multiply_numbers(num1, num2):
    try:
        result = float(num1) * float(num2)
        return result
    except ValueError:
        return "Error: Invalid input. Please provide numeric values."
if __name__ == '__main__':
    input_data = ["10", "5", "abc"]
    if len(input_data) >= 2:
        num1_str = input_data[0]
        num2_str = input_data[1]
        result = multiply_numbers(num1_str, num2_str)
        print(result)
    else:
        print("Not enough input provided.")