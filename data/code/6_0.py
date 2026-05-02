import sys
def calculate_difference(weight1, weight2):
    return abs(weight1 - weight2)
if __name__ == '__main__':
    weight1_input = 50.5
    weight2_input = 120.75
    try:
        weight1 = float(weight1_input)
        weight2 = float(weight2_input)
        if weight1 < 0 or weight2 < 0:
            print("Error: Weights cannot be negative.")
            sys.exit(1)
        difference = calculate_difference(weight1, weight2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers for weights.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)