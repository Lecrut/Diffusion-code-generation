def filter_greater_than_median(numbers):
    """
    Returns a new list containing elements greater than the median of the input list.
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: Elements strictly greater than the median value.
    """
    if not numbers:
        return []

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # Calculate median based on whether length is odd or even
    mid_index = (n - 1) // 2
    
    if n % 2 == 0:
        # For even lengths, Python's statistics.median uses the average of two middle values.
        # However, to compare elements directly for strict inequality (> median), 
        # we need a single float value as per standard statistical definition.
        lower = sorted_numbers[mid_index]
        upper = sorted_numbers[mid_index + 1]
        median_value = (lower + upper) / 2.0
    else:
        # For odd lengths, the middle element is the exact median.
        median_value = float(sorted_numbers[mid_index])

    return [num for num in numbers if num > median_value]

if __name__ == '__main__':
    sample_data = [3, 1, 4, 5, 2, 6, 8, 7]
    
    result = filter_greater_than_median(sample_data)
    
    print("Input:", sample_data)
    print("Output (elements > median):", result)