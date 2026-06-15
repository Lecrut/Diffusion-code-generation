import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py num1 num2")
else:
        try:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            if num1 > num2:
                print(f"{num1} is greater than {num2}")
            elif num1 < num2:
                print(f"{num1} is less than {num2}")
            else:
                print(f"{num1} is equal to {num2}")
        except ValueError:
            print("Invalid input. Please provide integers.")