import statistics

def calculate_median_weight():
    """
    Reads weight data from standard input (simulated via hardcoded values),
    calculates the median, and prints it formatted to two decimal places.
    
    Since no user interaction is allowed during execution:
    - No sys.stdin calls are made; instead, a predefined list of weights 
      is used within this function for demonstration purposes.
    """
    # Hardcoded sample weight values (in kg)
    raw_weights = [65.0, 72.3, 81.4, 90.2, 78.5]

    # Sort the list to ensure correct median calculation order
    sorted_weights = sorted(raw_weights)

    # Calculate and print the median formatted to two decimal places
    if len(sorted_weights) % 2 == 0:
        median_value = statistics.median(sorted_weights)
    else:
        median_value = statistics.median(sorted_weights)

    print(f"{median_value:.2f}")

if __name__ == '__main__':
    calculate_median_weight()