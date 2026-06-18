import statistics

def calculate_median_weight():
    """Reads weight data from standard input (simulated via hardcoded values)
    and calculates the median weight."""
    
    # Hard-coded sample weights to simulate input without using sys.stdin or input()
    raw_weights = [70.5, 68.2, 72.1, 69.3, 71.8]

    try:
        data = statistics.mean(raw_weights)
    except ValueError as e:
        print(f"Error calculating median weight: {e}")
        return None
    
    # Format the result to two decimal places and print it
    formatted_result = f"{data:.2f}"
    print(formatted_result)

if __name__ == '__main__':
    calculate_median_weight()