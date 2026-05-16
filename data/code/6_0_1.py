import sys
def calculate_difference(weight1, weight2):
    return abs(weight1 - weight2)
if __name__ == '__main__':
    weight1 = 50.5
    weight2 = 120.75
    try:
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise ValueError("Inputs must be numeric values.")
        difference = calculate_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)