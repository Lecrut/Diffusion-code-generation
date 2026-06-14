import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <number1> <number2>")
    else:
        try:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            result = num1 + num2
            print(result)
        except ValueError:
            print("Invalid input. Please provide integers.")