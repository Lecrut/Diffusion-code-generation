def calculate_ratio(a: float, b: float) -> None:
    """Prints the ratio of two positive numbers."""
    if a <= 0 or b <= 0:
        raise ValueError("Both measurements must be positive numbers.")
    
    result = a / b
    print(f"{a} : {b} = {result}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    measurement_a = 10.5
    measurement_b = 2
    
    try:
        calculate_ratio(measurement_a, measurement_b)
    except ValueError as e:
        print(f"Error: {e}")