import sys
def multiply_numbers(num1, num2):
    return num1 * num2
if __name__ == '__main__':
    try:
        num1 = 10
        num2 = 5
        result = multiply_numbers(num1, num2)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)