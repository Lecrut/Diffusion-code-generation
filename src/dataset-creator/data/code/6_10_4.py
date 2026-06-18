def calculate_product(num1, num2):
    return num1 * num2
if __name__ == '__main__':
    sample_num1 = 15
    sample_num2 = 7
    try:
        num1 = float(sample_num1)
        num2 = float(sample_num2)
        if num1 < 0 or num2 < 0:
            print("Error: Numbers cannot be negative.")
        else:
            product = calculate_product(num1, num2)
            print(product)
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")