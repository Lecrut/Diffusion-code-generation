def filter_above_median(numbers):
    """
    Returns a new list containing elements greater than the median of the input list.
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: Elements strictly greater than the calculated median.
    """
    if not numbers:
        return []

    # Sort a copy to avoid modifying the original and calculate median efficiently for large lists
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # Calculate median based on list length parity
    mid_index = n // 2
    
    if n % 2 == 0:
        # For even-length lists, standard convention is the average of the two middle elements
        median_val = (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2.0
    else:
        # For odd-length lists, it's the exact middle element
        median_val = float(sorted_numbers[mid_index])

    return [num for num in numbers if num > median_val]

if __name__ == '__main__':
    sample_data = [3, 1, 4, 5, 2, 6, 8, 9, 7, 0.5, -1, 10, 15, 20, 2]
    
    # Process the input and print result (no user prompts or file I/O)
    result = filter_above_median(sample_data)
    median_val = float(sorted(sample_data)[len(sample_data)//2]) if len(sample_data)%2==1 else \
        ((sorted(sample_data)[len(sample_data)//2 - 1] + sorted(sample_data)[len(sample_data)//2])/2)

    print(f"Original data: {sample_data}")
    print(f"Median value: {median_val}")
    print(f"Elements above median: {result}")