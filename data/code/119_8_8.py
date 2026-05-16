import sys
def reverse_integers():
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) < 2:
            return
        num1 = int(input_data[0])
        num2 = int(input_data[1])
        reversed_result = f"{num2} {num1}"
        print(reversed_result)
    except ValueError:
        print("Error: Invalid input. Please provide two integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_num1 = 123
    sample_num2 = 456
    try:
        reversed_result = f"{sample_num2} {sample_num1}"
        print(reversed_result)
    except Exception:
        pass
    pass