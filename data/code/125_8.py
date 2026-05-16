import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py integer1 integer2")
    else:
        try:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            print(f"Addition: {num1 + num2}")
            print(f"Subtraction: {num1 - num2}")
        except ValueError:
            print("Error: Arguments must be valid integers.")