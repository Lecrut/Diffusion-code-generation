import statistics

# Hard-coded sample weight data as a list of floats
sample_weights = [70.5, 68.2, 72.1, 69.3, 71.4]

def calculate_median_weight(weight_list):
    """Calculates the median weight from a given list."""
    if not weight_list:
        return None
    sorted_weights = sorted(weight_list)
    n = len(sorted_weights)
    mid = n // 2
    
    # Calculate based on whether the number of elements is odd or even
    if n % 2 == 1:
        median = float(sorted_weights[mid])
    else:
        left_val = float(sorted_weights[mid - 1])
        right_val = float(sorted_weights[mid])
        median = (left_val + right_val) / 2
    
    return median

if __name__ == '__main__':
    # Process the hard-coded sample data to find and print the median
    result = calculate_median_weight(sample_weights)
    if result is not None:
        formatted_result = f"{result:.2f}"
        print(formatted_result)