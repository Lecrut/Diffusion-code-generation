import statistics

def filter_above_median(numbers):
    """
    Returns a new list containing only elements greater than the median of the input list.
    
    Args:
        numbers (list[int]): List of integers to process.
        
    Returns:
        list[int]: List of integers strictly greater than the calculated median.
    """
    if not numbers:
        return []

    # Calculate the median first for efficiency as per task requirement
    median = statistics.median(numbers)
    
    # Filter elements that are strictly greater than the median
    result = [num for num in numbers if num > median]
    
    return result

if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60, 75, 80, 90, 100]
    filtered_result = filter_above_median(sample_data)
    
    # Print the result to verify functionality without user input or external dependencies
    print(f"Input list: {sample_data}")
    median_value = statistics.median(sample_data)
    print(f"Median value: {median_value}")
    print(f"Elements greater than median: {filtered_result}")