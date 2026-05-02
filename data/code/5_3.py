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
        return f"Error: {e}"
    except TypeError:
        return "Error: Invalid input type."
if __name__ == '__main__':
    measurement1 = "10.0"
    measurement2 = "2.5"
    result = calculate_ratio(measurement1, measurement2)
    print(result)