import sys
def calculate_sum(num1, num2, num3):
    return num1 + num2 + num3
if __name__ == '__main__':
    number1 = 10
    number2 = 25
    number3 = 5
    try:
        if not all(isinstance(n, int) for n in [number1, number2, number3]):
            raise ValueError("All inputs must be integers.")
        total_sum = calculate_sum(number1, number2, number3)
        print(f"The sum of {number1}, {number2}, and {number3} is: {total_sum}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)