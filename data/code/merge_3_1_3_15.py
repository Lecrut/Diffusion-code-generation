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
        dict[str, int]: A dictionary containing counts and list of outliers 
                        categorized by 'underweight', 'overweight', or 'normal'.
    
    Complexity Analysis:
        Time Complexity: O(n) where n is the number of weight entries. Each entry is visited once.
        Space Complexity: O(1) auxiliary space for counters, excluding input/output storage.
    """
    underweight_count = 0
    overweight_count = 0
    
    # Initialize lists to store outlier values if needed later (optional optimization based on use case)
    outliers_list = []

    for weight in weight_entries:
        is_outlier = False
        
        # Check conditions efficiently without redundant comparisons when possible
        if min_weight <= weight and max_weight >= weight:
            pass  # Within range, continue to next iteration
        elif weight < min_weight:
            underweight_count += 1
            outliers_list.append(weight)
            is_outlier = True
        else:  # Weight > max_weight
            overweight_count += 1
            outliers_list.append(weight)
            is_outlier = True
            
    return {
        "underweight": {"count": underweight_count, "values": outliers_list},
        "overweight": {"count": overweight_count, "values": outliers_list} # Note: 'outliers_list' contains all collected values. 
                         # To separate them strictly by category in a single pass without storing twice:
    }

# Optimized version to avoid duplicate list storage logic for clarity and efficiency
def find_outlier_weights_v2(weight_entries: list[float], min_weight: float = 50, max_weight: float = 200) -> dict[str, int]:
    """
    Efficiently processes weight entries returning counts of outliers.
    
    Args:
        weight_entries (list[float]): List of numerical weights.
        min_weight (float): Lower bound of acceptable range (inclusive).
        max_weight (float): Upper bound of acceptable range (inclusive).

    Returns:
        dict[str, int]: Dictionary with keys 'underweight_count', 'overweight_count'.
    
    Complexity Analysis:
        Time Complexity: O(n) - Single pass through the list.
        Space Complexity: O(1) - Only integer counters used.
    """
    underweight_count = 0
    overweight_count = 0
    
    for weight in weight_entries:
        if min_weight <= weight and max_weight >= weight:
            continue
        
        elif weight < min_weight:
            underweight_count += 1
            
        else: # Weight > max_weight
            overweight_count += 1
            
    return {
        "underweight_count": underweight_count,
        "overweight_count": overweight_count
    }

if __name__ == '__main__':
    # Hard-coded sample values representing a large dataset simulation.
    # Includes weights within range [50, 200], below 50, and above 200.
    
    raw_data = [60, 75, 45, 180, 90, 30, 210, 150, 55, 25] 
    # Expanded list to simulate "large dataset" performance characteristics without actual large file I/O
    sample_dataset = [60.5, 74.2, 88.9, 49.1, 35.0, 100.0, 201.5, 199.9, 
                      50.0, 200.0, 65.3, 70.1, 85.6, 48.2, 32.5, 185.7,
                      92.4, 110.0, 125.5, 140.2]

    # Run the efficient algorithm (v2 for minimal memory overhead)
    results = find_outlier_weights_v2(sample_dataset)

    print("Weight Analysis Report")
    print(f"Total entries processed: {len(sample_dataset)}")
    
    underweight_result = f"{results['underweight_count']} measurements were below 50 kg."
    overweight_result = f"{results['overweight_count']} measurements exceeded 200 kg."

    if results["underweight_count"] > 0 or results["overweight_count"] > 0:
        print(f"\nOutliers detected:")
        print(underweight_result)
        print(overweight_result)
        
        # Optional statistical insight for the dataset as a whole (not part of outlier logic but useful context)
        avg_weight = statistics.mean(sample_dataset) if sample_dataset else 0
        median_weight = statistics.median(sample_dataset) if sample_dataset else 0
        
        print(f"\nDataset Statistics:")
        print(f"Average weight: {avg_weight:.2f} kg")
        print(f"Median weight: {median_weight:.2f} kg")
    else:
        print("\nAll measurements are within the acceptable range.")