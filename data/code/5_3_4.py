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
    measurement1_str = "10.0"
    measurement2_str = "2.5"
    try:
        result = calculate_ratio(measurement1_str, measurement2_str)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)