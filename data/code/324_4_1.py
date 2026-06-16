def calculate_product(num1, num2):
    try:
        result = float(num1) * float(num2)
        print(f"The product is: {result}")
    except ValueError:
        print("Error: Both inputs must be valid numbers.")
if __name__ == '__main__':
    input_str1 = "10"
    input_str2 = "5"
    calculate_product(input_str1, input_str2)