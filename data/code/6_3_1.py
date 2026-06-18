def get_weight_difference():
    """Reads two weights from standard input (simulated via hard-coded values in main)
    and prints their difference with error handling."""
    
    # Simulating user input by generating sample strings to test functionality
    try:
        weight1_str = "75.5"
        weight2_str = "68.3"
        
        weight1 = float(weight1_str)
        weight2 = float(weight2_str)
        
        difference = weight1 - weight2
        
        print(f"{difference:.4f}")
    except ValueError:
        # Handles cases where input is not a valid number
        raise Exception("Error: Non-numeric input detected.")

if __name__ == '__main__':
    try:
        get_weight_difference()
    except Exception as e:
        print(e)