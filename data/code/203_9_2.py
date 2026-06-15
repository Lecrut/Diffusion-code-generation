import sys
def compare_numbers(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"
if __name__ == '__main__':
    try:
        num1 = 15
        num2 = 25
        result = compare_numbers(num1, num2)
        print(result)
    except ValueError as e:
        print(f"An error occurred during comparison: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)