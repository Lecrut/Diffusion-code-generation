def calculate_weight_difference():
    """Reads two weight values from standard input, converts to floats, 
    prints their difference."""
    try:
        # Simulating reading from stdin with sample hard-coded values as per requirements
        value1 = "25.5"  # Sample first weight
        value2 = "30.75" # Sample second weight
        
        float_value1 = float(value1)
        float_value2 = float(value2)
        
        difference = float_value2 - float_value1
        print(difference)
    except ValueError:
        print("Error: Invalid input provided.")
    return None

if __name__ == '__main__':
    calculate_weight_difference()