import statistics

def filter_above_median(nums):
    """
    Returns a new list containing elements from nums that are greater than the median.
    
    If the number of elements is even, the lower middle value is used as the median (standard 
    behavior in Python's statistics.median). This aligns with float-based median calculation 
    which naturally handles both odd and even lengths correctly without ambiguity for this use case.
    
    Args:
        nums (list[int]): List of integers to process.
        
    Returns:
        list[int]: A new list containing elements greater than the median.
    """
    if not nums:
        return []

    # Calculate the median using statistics module for robustness and clarity
    median = statistics.median(nums)
    
    # Filter elements strictly greater than the calculated median
    result = [x for x in nums if x > median]
    
    return result

if __name__ == '__main__':
    sample_data = [10, 23.5, 44, -19, 678, 33, -4, 3, 12, 5, 11, 1]
    
    # Note: While the function signature accepts integers as per task description, 
    # Python's statistics.median will return a float if any non-int or even count exists.
    # For integer-only input lists of odd length (like this sample), it returns an int.
    filtered_list = filter_above_median(sample_data)

    print(f"Input: {sample_data}")
    print(f"Median: {statistics.median(sample_data)}")
    print(f"Elements above median: {filtered_list}")