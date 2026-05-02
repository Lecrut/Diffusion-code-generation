import sys
def calculate_ratio(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        if num_a > 0 and num_b > 0:
            return num_a / num_b
        else:
            raise ValueError("Measurements must be positive.")
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")
if __name__ == '__main__':
    input_data = ["10.0", "2.0"]
    if len(input_data) != 2:
        print("Error: Expected two inputs.", file=sys.stderr)
    else:
        try:
            measurement1 = input_data[0]
            measurement2 = input_data[1]
            result = calculate_ratio(measurement1, measurement2)
            print(result)
        except ValueError as e:
            print(f"Error calculating ratio: {e}", file=sys.stderr)