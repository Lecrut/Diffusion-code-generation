import sys
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) == 2:
            num1 = int(input_data[0])
            num2 = int(input_data[1])
            if num1 > num2:
                print(f"{num1} {num2}")
            else:
                print(f"{num2} {num1}")
        else:
            print("Error: Expected two space-separated integers.")
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")