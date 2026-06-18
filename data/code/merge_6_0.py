import sys
def calculate_product(num1, num2):
    return num1 * num2
if __name__ == '__main__':
    try:
        input_str1 = "10"
        input_str2 = "5"
        num1 = int(input_str1)
        num2 = int(input_str2)
        if num1 < 0 or num2 < 0:
            print("Error: Numbers cannot be negative.")
        else:
            product = calculate_product(num1, num2)
            print(product)
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")