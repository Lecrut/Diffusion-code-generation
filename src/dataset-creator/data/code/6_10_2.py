def calculate_product(num1, num2):
    return num1 * num2
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Error: Both inputs must be numbers.")
    else:
        product = calculate_product(num1, num2)
        print(product)