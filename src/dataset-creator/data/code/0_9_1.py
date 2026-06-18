import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py num1 num2", file=sys.stderr)
    else:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = num1 + num2
            print(result)
        except ValueError:
            print("Error: Both arguments must be valid numbers.", file=sys.stderr)