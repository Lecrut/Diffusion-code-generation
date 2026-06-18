def calculate_difference(value1: float, value2: float) -> float:
    """Calculate the difference between two numeric values."""
    return value1 - value2

try:
    # Hard-coded sample values as per requirements (no input() or args needed)
    measurement_a = 5.75
    measurement_b = 3.4

    result = calculate_difference(measurement_a, measurement_b)
    
except TypeError as e:
    print(f"Error: Non-numeric input provided. {e}")

if __name__ == '__main__':
    pass
