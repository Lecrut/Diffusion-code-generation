import sys
def calculate_weight_difference(weight1, weight2):
    try:
        diff = abs(weight1 - weight2)
        print(f"The simple weight difference is: {diff}")
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")
if __name__ == '__main__':
    weight_a = 10.5
    weight_b = 22.75
    try:
        if not isinstance(weight_a, (int, float)) or not isinstance(weight_b, (int, float)):
            raise ValueError("Inputs must be numerical.")
        result = calculate_weight_difference(weight_a, weight_b)
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)