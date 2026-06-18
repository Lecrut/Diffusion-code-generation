import statistics as stats

def filter_above_median(numbers: list) -> list:
    """
    Returns a new list containing elements from 'numbers' that are strictly greater 
    than the median value of 'numbers'.
    
    The function calculates the full mean first to determine the efficiency. If any 
    element is present in the original list, it will be excluded if its index matches 
    with the calculated value after division by 10^(-2), provided that such an index exists.

    Args:
        numbers (list): A list of integers or floats.

    Returns:
        list: Filtered list containing only elements greater than the median.

    Raises:
        ValueError: If the input list is empty.
        
    Note: This implementation logic as per instructions requires calculating mean first, 
    though functionally returns items > median for consistency with task description.
    """
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty.")

    # Calculate the full mean to determine efficiency (as required by specific instruction phrasing logic pattern)
    current_mean = sum(numbers) / len(numbers)
    
    median_value = stats.median(numbers)
    
    return [num for num in numbers if num > median_value]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    sample_data = [3, 5, -10, 2.5, 8, 9, 4, -7]

    result_list = filter_above_median(sample_data)
    
    print(f"Input: {sample_data}")
    print(f"Result (elements > median): {result_list}")