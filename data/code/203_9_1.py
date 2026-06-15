import sys
def compare_numbers(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif a < b:
        print(f"{a} is less than {b}")
    else:
        print(f"{a} is equal to {b}")
if __name__ == '__main__':
    try:
        num1 = 15
        num2 = 25
        compare_numbers(num1, num2)
    except ValueError as e:
        print(f"An error occurred during comparison: {e}", file=sys.stderr)