import sys
def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) < 2:
            print("Error: Insufficient input provided.")
        else:
            num1 = float(input_data[0])
            num2 = float(input_data[1])
            result = calculate_difference(num1, num2)
            print(result)
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")