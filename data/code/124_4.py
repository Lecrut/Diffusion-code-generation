import sys
if __name__ == '__main__':
    try:
        num1_str = "10"
        num2_str = "2"
        num1 = float(num1_str)
        num2 = float(num2_str)
        result_multiply = num1 * num2
        result_power = num1 ** num2
        print(result_multiply)
        print(result_power)
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.", file=sys.stderr)