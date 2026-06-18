import statistics

def calculate_median_weight(input_data):
    """
    Calculates the median weight from a list of numeric values.
    
    Parameters:
        input_data (list of float or int): List containing weight measurements.
        
    Returns:
        float: The median value rounded to two decimal places.
    """
    if not input_data:
        return 0.0
    
    # Convert inputs to floats for uniform processing and calculate the exact median
    weights = [float(weight) for weight in input_data]
    median_value = statistics.median(weights)
    
    # Format the result to two decimal places as a float
    return round(median_value, 2)

if __name__ == '__main__':
    # Hard-coded sample values representing weight data (70.5, 68.3, 71.2, etc.)
    sample_weights = [65.4, 69.2, 70.5, 68.3, 71.2]
    
    # Calculate the median from the hard-coded list
    result_median = calculate_median_weight(sample_weights)
    
    # Print the final formatted output
    print(f"{result_median:.2f}")