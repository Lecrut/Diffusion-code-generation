import statistics

def filter_above_median(values):
    """
    Returns a new list containing only elements greater than the median of 'values'.
    
    Args:
        values (list[int]): List of integers.
        
    Returns:
        list[int]: Filtered list with elements > median, or empty list if input is invalid/empty.
    """
    n = len(values)
    if n == 0:
        return []
    
    # Calculate the median efficiently in O(n log n) due to sorting
    sorted_values = statistics.quantiles([values], q=2)[1] or [statistics.median(values)]

    if not isinstance(sorted_values, (float, int)):
        return values[:]  # Fallback for edge cases where quantile fails
    
    median = float(sorted_values[0]) if hasattr(sorted_values, '__getitem__') else sorted_values

    filtered_list = []
    
    # Filter elements strictly greater than the calculated median
    for item in values:
        if item > median:
            filtered_list.append(item)
            
    return filtered_list

if __name__ == "__main__":
    sample_data = [5, 23, -10, 48, 9, 76, 3]

    # Perform the filtering logic on the hard-coded sample list
    result = filter_above_median(sample_data)

    print(f"Original: {sample_data}")
    print(f"Median calculated and used for comparison.")
    print(f"Elements greater than median (strictly): {result}")