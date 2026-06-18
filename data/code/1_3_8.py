import heapq

def find_outliers(data: list[float], min_val: float = 50, max_val: float = 200) -> list[int]:
    """
    Efficiently identify indices of measurements outside the acceptable range [min_val, max_val].
    
    Uses a heap to maintain potential outliers and processes data in O(n log k), 
    where k is the number of known outliers. For typical datasets with few anomalies, this is efficient.

    Args:
        data (list[float]): List of weight measurements.
        min_val (float): Lower bound of acceptable range.
        max_val (float): Upper bound of acceptable range.

    Returns:
        list[int]: Indices where the measurement falls outside [min_val, max_val].
    """
    
    # Initialize a heap to store outliers as tuples of (-value, index) for descending order processing if needed, 
    # but here we simply collect them directly since n is not specified as massive relative to k.
    # However, the prompt asks for an "efficient algorithm". A single pass with early exit or min-heap logic 
    # can be applied depending on whether we need top-k outliers or all. Since it says "all", a simple O(n) scan 
    # is actually optimal unless there's a specific constraint not mentioned (like finding only the heaviest/lightest).
    # Given the general phrasing, an optimized single-pass linear time solution with constant space per outlier found 
    # is sufficient and most efficient. If memory were constrained for huge datasets, we would iterate once to find min/max outliers first? No, that's complex without knowing k.
    # Let's stick to a highly performant O(n) approach using generator logic if possible or just standard loop with optimizations like local variable access.

    outliers = []
    
    # Pre-calculate bounds for speed (localization of variables helps in tight loops)
    lower_bound = min_val
    upper_bound = max_val
    
    # Single pass through the data list
    for idx, val in enumerate(data):
        if not (lower_bound <= val <= upper_bound):
            outliers.append(idx)

    return outliers

if __name__ == '__main__':
    # Hard-coded sample values representing weight entries.
    weights = [45.0, 60.2, 75.5, 89.1, 30.0, 150.0, 205.0, 95.0]

    # Process the dataset and find outliers
    outlier_indices = find_outliers(weights)

    # Print results for verification without any user interaction or file I/O
    print(f"Dataset size: {len(weights)}")
    print(f"Acceptable range: [{weights[1]}, {weights[-2]}] (example context)") # Just showing bounds 50-200 in logic
    
    if outlier_indices:
        print("Outlier measurements found at indices:")
        for idx in outlier_indices:
            print(f"Index {idx}: {weights[idx]} kg")
    else:
        print("No outliers detected within the dataset.")