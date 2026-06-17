import sys
def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    try:
        sample_num1 = 25
        sample_num2 = 10
        if not isinstance(sample_num1, (int, float)) or not isinstance(sample_num2, (int, float)):
            raise ValueError("Both inputs must be numeric.")
        difference = calculate_difference(sample_num1, sample_num2)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)