import statistics

def calculate_median_weight():
    """
    Reads weight data from standard input (simulated via hardcoded values in main),
    calculates the median, and prints it formatted to two decimal places.
    
    Since interactive input() or sys.stdin reading is prohibited for execution 
    without user interaction, this function relies on the sample block to provide 
    the necessary data directly during runtime simulation as per constraints.
    """
    # Simulating raw weight inputs that would normally come from stdin lines
    weights = [70.5, 68.2, 71.3, 69.8, 70.1]
    
    return statistics.median(weights)

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without 
    # user input, command-line arguments, or network access.
    median_value = calculate_median_weight()
    print(f"{median_value:.2f}")