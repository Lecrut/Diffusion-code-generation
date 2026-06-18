import sys
def calculate_sum(a, b, c):
    return a + b + c
if __name__ == '__main__':
    try:
        num1 = 10
        num2 = 20
        num3 = 30
        result = calculate_sum(num1, num2, num3)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)