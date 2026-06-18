import statistics

def find_outlier_weights(weight_entries: list[float], min_weight: float = 50, max_weight: float = 200) -> list[int]:
    """
    Identifies indices of weight entries that fall outside the acceptable range [min_weight, max_weight].
    
    Args:
        weight_entries (list): List of numerical weights.
        min_weight (float): Lower bound of the acceptable range (inclusive).
        max_weight (float): Upper bound of the acceptable range (inclusive).
        
    Returns:
        list[int]: A list containing indices where weights are out of bounds, sorted in ascending order.
    """
    outliers = []
    
    # Iterate through each entry with its index to check against the defined limits
    for idx, weight in enumerate(weight_entries):
        if not (min_weight <= weight <= max_weight):
            outliers.append(idx)
            
    return outliers

if __name__ == '__main__':
    # Hard-coded sample dataset representing weights in kg
    SAMPLE_WEIGHTS = [52.0, 48.5, 199.8, 60.0, 30.0, 150.0, 210.0]

    # Define acceptable range boundaries
    MIN_ACCEPTABLE_KG = 50.0
    MAX_ACCEPTABLE_KG = 200.0
    
    # Process the dataset and retrieve outlier indices
    invalid_indices = find_outlier_weights(SAMPLE_WEIGHTS, MIN_ACCEPTABLE_KG, MAX_ACCEPTABLE_KG)

    # Output results for verification without external input or files
    print(f"Dataset processed: {len(SAMPLE_WEIGHTS)} entries")
    print(f"Acceptable range: [{MIN_ACCEPTABLE_KG}, {MAX_ACCEPTABLE_KG}] kg")
    
    if invalid_indices:
        print("Measurements outside acceptable range (indices):", invalid_indices)
        
        # Display the actual values associated with these indices for clarity
        outlier_values = [SAMPLE_WEIGHTS[i] for i in invalid_indices]
        print(f"Outlier weight values: {outlier_values} kg")
    else:
        print("All measurements are within acceptable range.")