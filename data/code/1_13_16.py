import statistics

def calculate_median_weight(weight_data):
    """Calculates the median weight from a list of numeric values."""
    return round(statistics.median(weight_data), 2)

if __name__ == '__main__':
    # Hard-coded sample weights for testing without user input
    raw_weights = [65.0, 70.5, 80.3, 45.2, 90.1]

    median_weight = calculate_median_weight(raw_weights)
    
    print(f"{median_weight:.2f}")