import sys
def compare_numbers(a, b):
    if a > b:
        return True
    else:
        return False
if __name__ == '__main__':
    try:
        input_str_a = "10"
        input_str_b = "5"
        num_a = int(input_str_a)
        num_b = int(input_str_b)
        result = compare_numbers(num_a, num_b)
        if result:
            print("First number is strictly greater than the second number.")
        else:
            print("First number is not strictly greater than the second number.")
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")