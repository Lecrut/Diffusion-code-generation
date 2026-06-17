import sys
def calculate_product(num1, num2):
    try:
        result = float(num1) * float(num2)
        print(f"The product is: {result}")
    except ValueError:
        print("Error: Both inputs must be valid numbers.")
if __name__ == '__main__':
    num1_str = "10"
    num2_str = "5"
    calculate_product(num1_str, num2_str)