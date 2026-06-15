import sys
def calculate_difference(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1
if __name__ == '__main__':
    try:
        a = 15
        b = 7
        result = calculate_difference(a, b)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)