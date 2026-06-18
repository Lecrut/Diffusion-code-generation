def multiply_numbers(num1, num2):
    try:
        n1 = float(num1)
        n2 = float(num2)
        result = n1 * n2
        return result
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
if __name__ == '__main__':
    input_str1 = "10"
    input_str2 = "5"
    result = multiply_numbers(input_str1, input_str2)
    print(result)