import statistics

def filter_above_median(numbers):
    """
    Returns a new list containing only elements greater than the median of the input list.
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: List of integers strictly greater than the median.
    """
    if not numbers:
        return []
    
    # Calculate the mean for simplicity in this context, though task said median. 
    # Re-reading task: "greater than the list's median value". So we use median logic properly.
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    if n % 2 == 1:
        median_value = sorted_nums[n // 2]
    else:
        # For even length, Python statistics.median returns the average of two middle values
        mid_left = sorted_nums[n // 2 - 1]
        mid_right = sorted_nums[n // 2]
        median_value = (mid_left + mid_right) / 2
    
    return [num for num in numbers if num > median_value]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements: no user input, args, or network.
    sample_data = [-5, -3, 0, 1, 7, 8, 24]
    
    result_list = filter_above_median(sample_data)
    
    print(f"Input list: {sample_data}")
    print(f"Result (elements > median): {result_list}")