import statistics

def filter_above_median(numbers):
    """
    Returns a new list containing elements from 'numbers' that are strictly greater 
    than the median of the original list.
    
    The median is calculated first to avoid sorting multiple times if needed, though
    calculating it requires sorting anyway for an even-length list (average of two middle values).

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        list[int]: List of elements greater than the median.
    
    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    
    # Calculate the median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid_index = n // 2
    
    if n % 2 == 1:
        # Odd length: middle element is the median
        median_value = sorted_numbers[mid_index]
    else:
        # Even length: average of two middle elements
        median_value = (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
    
    # Filter elements strictly greater than the median
    result = [num for num in numbers if num > median_value]
    
    return result

if __name__ == '__main__':
    sample_data = [3, 7, 5, 10, 4, 8, 2, 9]
    filtered_result = filter_above_median(sample_data)
    print(f"Input: {sample_data}")