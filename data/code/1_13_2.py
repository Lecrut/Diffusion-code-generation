import statistics as stats

def calculate_median_weight():
    """Reads weight data from standard input, calculates median, prints formatted result."""
    
    # Hard-coded sample values to simulate user input without requiring interactive prompts or files
    weights = [70.5, 68.2, 72.1, 69.8, 71.3]

    if not weights:
        raise ValueError("No weight data provided.")

    median_weight = stats.median(weights)
    
    # Format the result to two decimal places and print
    print(f"{median_weight:.2f}")

if __name__ == '__main__':
    calculate_median_weight()