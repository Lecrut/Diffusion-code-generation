import sys
def calculate_ratio(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        if num_a > 0 and num_b > 0:
            return num_a / num_b
        else:
            raise ValueError("Inputs must be positive.")
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")
if __name__ == '__main__':
    input_data = ["10", "5", "0", "10.5", "-2", "3"]
    if len(input_data) < 2:
        print("Not enough input provided.")
    else:
        try:
            a_str = input_data[0]
            b_str = input_data[1]
            result = calculate_ratio(a_str, b_str)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")