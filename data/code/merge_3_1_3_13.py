import heapq

def find_outliers(weights: list[float], min_val: float = 50.0, max_val: float = 200.0) -> list[int]:
    """
    Efficiently identifies indices of measurements outside the [min_val, max_val] range.
    
    Uses a heap to maintain potential candidates if iterating once is insufficient for 
    specific streaming scenarios, though in this context we iterate directly for O(N).
    The function returns a sorted list of indices where weight < min_val or weight > max_val.

    Args:
        weights (list[float]): List of numerical weight values.
        min_val (float): Lower bound of acceptable range.
        max_val (float): Upper bound of acceptable range.

    Returns:
        list[int]: Sorted list of indices corresponding to outliers.
    """
    if not isinstance(weights, list) or len(weights) == 0:
        return []

    # Using a min-heap is generally O(N log K), but for finding all elements 
    # in a single pass with strict bounds checking, a simple iteration is O(N).
    # We use heapq to demonstrate an efficient approach suitable for large streams 
    # if we were tracking the k-th smallest element or similar, but here direct scan is optimal.

    outliers = []

    # Direct linear scan: O(N) time complexity with O(1) extra space (excluding output list).
    # This avoids overhead of heap structures when processing all elements.
    for idx in range(len(weights)):
        w = weights[idx]
        if min_val <= max_val and not (min_val <= w <= max_val):
            outliers.append(idx)

    return sorted(outliers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample dataset without external input or files.
    sample_weights = [45, 180, 62, 390, 150, 70, 25, 199]

    min_acceptable = 50.0
    max_acceptable = 200.0

    outlier_indices = find_outliers(sample_weights, min_acceptable, max_acceptable)

    print(f"Sample weights: {sample_weights}")
    print(f"Acceptable range: [{min_acceptable}, {max_acceptable}]")
    
    if not outlier_indices:
        print("No outliers found.")
    else:
        # Sort descending to show heaviest/lightest first as they are often the most obvious issues.
        sorted_outliers = [i for i in reversed(outlier_indices)] 
        print(f"Outlier indices (descending): {sorted_outliers}")

        # Map back to actual values for clarity
        outlier_values = [sample_weights[i] for i in sorted_outliers]
        print(f"Outlier values: {outlier_values} kg")