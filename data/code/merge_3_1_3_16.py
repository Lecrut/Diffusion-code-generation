import statistics

def find_outlier_weights(entries: list[float], min_weight: float = 50, max_weight: float = 200) -> list[int]:
    """
    Identifies indices of weight entries that fall outside the acceptable range [min_weight, max_weight].
    
    Args:
        entries (list[float]): List of weight measurements.
        min_weight (float): Lower bound of the acceptable range (inclusive).
        max_weight (float): Upper bound of the acceptable range (inclusive).
        
    Returns:
        list[int]: A list of indices where weights are out of bounds.
    """
    outlier_indices = []
    
    # Iterate through each entry with its index to check against the predefined range
    for idx, weight in enumerate(entries):
        if not (min_weight <= weight <= max_weight):
            outlier_indices.append(idx)
            
    return outlier_indices

if __name__ == '__main__':
    # Hard-coded sample dataset of weights in kg
    sample_weights = [52.0, 48.5, 195.0, 60.0, 210.0, 75.3, 49.9, 180.2]
    
    # Define acceptable range (default: 50 to 200 kg)
    MIN_ACCEPTABLE = 50
    MAX_ACCEPTABLE = 200
    
    # Process the dataset and find outliers
    outlier_indices = find_outlier_weights(sample_weights, MIN_ACCEPTABLE, MAX_ACCEPTABLE)
    
    print(f"Dataset processed. Found {len(outlier_indices)} measurements outside the range [{MIN_ACCEPTABLE}, {MAX_ACCEPTABLE}].")
    for idx in outlier_indices:
        weight_value = sample_weights[idx]
        status = "underweight" if weight_value < MIN_ACCEPTABLE else "overweight"
        print(f"Index {idx}: Weight is {weight_value:.2f} kg ({status})")

    # Optional statistical summary of the full dataset for context (not part of outlier logic)
    try:
        mean_weight = statistics.mean(sample_weights) if sample_weights else 0.0
        std_deviation = statistics.stdev(sample_weights) if len(sample_weights) > 1 else 0.0
        
        print(f"\nDataset Statistics:")
        print(f"Total entries: {len(sample_weights)}")
        print(f"Mean weight: {mean_weight:.2f} kg")
        print(f"Standard deviation: {std_deviation:.2f} kg")
    except statistics.StatisticsError:
        pass  # Handle case with single element or empty list gracefully if needed later