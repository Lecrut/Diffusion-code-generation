import statistics

def find_outlier_weights(entries: list[float], min_weight: float = 50, max_weight: float = 200) -> list[int]:
    """
    Identifies indices of weight entries that fall outside the acceptable range [min_weight, max_weight].

    Args:
        entries (list[float]): A list of floating-point weights.
        min_weight (float): The lower bound of the acceptable range (inclusive). Default is 50 kg.
        max_weight (float): The upper bound of the acceptable range (inclusive). Default is 200 kg.

    Returns:
        list[int]: A sorted list of indices where weights are out of bounds.
    """
    outlier_indices = []
    
    # Iterate through entries to find outliers efficiently in a single pass
    for index, weight in enumerate(entries):
        if not (min_weight <= weight <= max_weight):
            outlier_indices.append(index)

    return sorted(outlier_indices)

if __name__ == '__main__':
    # Hard-coded sample dataset with various weights including outliers < 50 and > 200
    raw_data = [48.5, 95.0, 150.2, 3.7, 60.0, 210.5, 180.0, 50.0, 200.0]

    print("Original Weight Data:")
    for i, weight in enumerate(raw_data):
        status = "OUTLIER" if not (50 <= weight <= 200) else "OK"
        print(f"{i}: {weight} kg [{status}]")

    # Process the data using the algorithm
    outlier_indices = find_outlier_weights(raw_data, min_weight=50.0, max_weight=200.0)

    if len(outlier_indices) == 0:
        print("\nNo outliers detected.")
    else:
        print(f"\nFound {len(outlier_indices)} outlier(s). Indices: {outlier_indices}")
        
        # Verify the actual values of the outliers for clarity
        print("Outlier Details:")
        indices_set = set()  # To avoid duplicate printing if logic changes later, though list is unique here
        for idx in sorted(set(outlier_indices)):
            val = raw_data[idx]
            reason = "Below minimum" if val < 50 else "Above maximum"
            print(f"Index {idx}: Value {val} kg ({reason})")

    # Additional verification: Calculate mean of valid entries to ensure no division by zero later if needed
    try:
        valid_weights = [w for w in raw_data if 50 <= w <= 200]
        print(f"\nStatistics on Valid Entries:")
        print(f"Count: {len(valid_weights)}")
        print(f"Mean (kg): {statistics.mean(valid_weights):.2f}")
    except ValueError:
        print("\nWarning: No valid entries found to calculate statistics.")