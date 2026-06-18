def multiply_numbers(num1, num2):
    result = num1 * num2
    return result
if __name__ == '__main__':
    sample_num1 = 15
    sample_num2 = 7
    try:
        num1 = int(sample_num1)
        num2 = int(sample_num2)
        product = multiply_numbers(num1, num2)
        print(product)
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")