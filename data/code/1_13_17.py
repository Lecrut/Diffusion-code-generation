import statistics

def calculate_median_weight():
    """Reads weight data from standard input (simulated via sample values)
    calculates the median, and prints it formatted to two decimal places."""
    
    # Hard-coded sample values as per requirements: no interactive prompts or sys.stdin usage.
    sample_data = [65.4321, 70.1234, 89.5678, 54.3210, 90.0]

    # Using the statistics module for median calculation as requested.
    try:
        median_weight = statistics.median(sample_data)
        
        # Format to two decimal places and print the result.
        print(f"{median_weight:.2f}")
    
    except Exception as e:
        # In case of unexpected errors during processing, though unlikely with fixed data.
        raise RuntimeError(f"Error calculating median weight: {e}")

if __name__ == '__main__':
    calculate_median_weight()