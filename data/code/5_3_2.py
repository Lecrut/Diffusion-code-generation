import sys
def calculate_ratio(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        if num_a > 0 and num_b > 0:
            return num_a / num_b
        else:
            raise ValueError("Inputs must be positive numbers")
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")
if __name__ == '__main__':
    input_data = ["10.0", "2.0"]
    if len(input_data) != 2:
        print("Error: Expected two input values.", file=sys.stderr)
    else:
        try:
            result = calculate_ratio(input_data[0], input_data[1])
            print(result)
        except ValueError as e:
            print(f"Error calculating ratio: {e}", file=sys.stderr)