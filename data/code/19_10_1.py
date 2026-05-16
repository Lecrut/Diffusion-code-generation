import sys
def compare_numbers(a, b):
    if a > b:
        return True
    else:
        return False
if __name__ == '__main__':
    try:
        input_a = 10
        input_b = 5
        if not isinstance(input_a, int) or not isinstance(input_b, int):
            print("Error: Both inputs must be integers.")
            sys.exit(1)
        result = compare_numbers(input_a, input_b)
        if result:
            print("The first number is strictly greater than the second number.")
        else:
            print("The first number is not strictly greater than the second number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)