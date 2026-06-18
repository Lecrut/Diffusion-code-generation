"""
Script to compare two volume measurements provided as floating-point numbers.
The script prints a human-readable result indicating whether the first value is greater, 
less than, or equal to the second value, handling potential precision issues with floats.
No user input, command-line arguments, network access, or file I/O are used.
"""

def compare_volumes(value_a: float, value_b: float) -> None:
    """
    Compare two volume measurements and print the result in a human-readable format.

    This function handles floating-point comparison carefully by using an epsilon 
    to account for potential precision errors that might arise from standard arithmetic operations.
    
    Parameters:
        value_a (float): The first volume measurement.
        value_b (float): The second volume measurement.

    Returns:
        None: The result is printed directly to stdout.
    """
    # Define a small epsilon for floating-point comparison tolerance
    EPSILON = 1e-9
    
    if abs(value_a - value_b) < EPSILON:
        print(f"The volumes are effectively equal.")
    elif value_a > value_b + EPSILON:
        diff = round(value_a - value_b, decimal_places=6)
        print(f"{value_a} is greater than {value_b}. The difference is approximately {diff:.2f}.")
    else:
        diff = round(value_b - value_a, decimal_places=6)
        print(f"{value_a} is less than {value_b}. The difference is approximately {abs(diff):.2f}.")

if __name__ == '__main__':
    # Hard-coded sample values for testing purposes
    volume_alpha = 150.7894321
    volume_beta = 150.7894326
    
    print("--- Volume Comparison Test ---\n")
    
    compare_volumes(volume_alpha, volume_beta)