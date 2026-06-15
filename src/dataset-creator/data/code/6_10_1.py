import sys
def calculate_product(num1, num2):
    return num1 * num2
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    try:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Inputs must be numbers.")
        result = calculate_product(num1, num2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)