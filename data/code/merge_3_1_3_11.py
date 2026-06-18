import statistics

def find_outlier_weights(weight_entries: list[float], min_weight: float = 50, max_weight: float = 200) -> dict[str, int]:
    """
    Processes a large dataset of weight entries and identifies measurements 
    outside the acceptable range [min_weight, max_weight].

    Args:
        weight_entries (list[float]): List of numerical weights.
        min_weight (float): Lower bound of acceptable range (inclusive).
        max_weight (float): Upper bound of acceptable range (inclusive).

    Returns:
        dict[str, int]: Dictionary containing counts and list of outliers outside the specified range.
            Keys are 'underweight_count', 'overweight_count', 
            'total_outliers', and 'outlier_values'.
    """
    
    # Initialize counters for underweight (below min) and overweight (above max) entries
    underweight_count = 0
    overweight_count = 0
    
    # List to store the actual outlier values found in this dataset
    outlier_values = []

    # Iterate through each weight entry with a single pass O(n) complexity for efficiency
    for weight_entry in weight_entries:
        if weight_entry < min_weight or weight_entry > max_weight:
            underweight_count += 1 if weight_entry < min_weight else overweight_count + 1
            
            outlier_values.append(weight_entry)

    # Calculate total number of outliers found outside the range
    total_outliers = len(outlier_values)

    return {
        'underweight_count': underweight_count,
        'overweight_count': overweight_count,
        'total_outliers': total_outliers,
        'outlier_values': outlier_values
    }

if __name__ == '__main__':
    # Hard-coded sample values representing a large dataset of weight entries.
    # Includes various weights including those outside the 50-200 kg range for testing.
    sample_weights = [48, 60, 75, 90, 110, 130, 150, 180, 210, 250, 
                      55, 62, 70, 85, 100, 140, 160, 190,
                      45, 30, 20]

    # Process the dataset using the defined function with default range (50-200 kg)
    result = find_outlier_weights(sample_weights)

    # Output results to console for verification without external dependencies or prompts
    print("Weight Analysis Report")
    print(f"Total Underweight Entries (< 50kg): {result['underweight_count']}")
    print(f"Total Overweight Entries (> 200kg): {result['overweight_count']}")
    print(f"Total Outliers: {result['total_outliers']}")
    
    if result['outlier_values']:
        print("Outlier Values Found:")
        for val in result['outlier_values']:
            marker = " (Under)" if val < 50 else " (Over)"
            print(f"  - {val} kg{marker}")