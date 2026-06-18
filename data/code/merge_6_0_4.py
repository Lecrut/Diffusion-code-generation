import sys
def calculate_product(num1, num2):
    return num1 * num2
if __name__ == '__main__':
    try:
        num1 = 15
        num2 = 7
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            print("Error: Both inputs must be numbers.")
            sys.exit(1)
        result = calculate_product(num1, num2)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")