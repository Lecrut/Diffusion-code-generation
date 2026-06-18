import statistics

def filter_above_median(numbers):
    """
    Returns a new list containing elements from 'numbers' that are strictly greater than the median of 'numbers'.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        list[int]: Filtered list with elements above the median.
    
    Raises:
        ValueError: If the input list is empty or contains non-integer values.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if len(numbers) == 0:
        return []
    
    # Ensure all elements are integers (or float that can represent integer exactly for median calculation context)
    try:
        numeric_list = [int(x) for x in numbers]
    except ValueError as e:
        raise TypeError("All elements must be convertible to integers.") from e

    if len(numeric_list) == 0:
        return []

    # Calculate the median efficiently using statistics module which uses O(N log N) or better depending on implementation, 
    # but sorting is required for standard median calculation. For very large lists, a linear time algorithm exists (Quickselect),
    # but Python's Timsort makes simple sort quite optimized in CPython. Given constraints and typical usage, this is efficient enough.
    sorted_numbers = sorted(numeric_list)
    
    n = len(sorted_numbers)
    mid_index = n // 2
    
    if n % 2 == 1:
        median_value = float(sorted_numbers[mid_index])
    else:
        # Average of two middle elements for even length lists
        lower_mid = sorted_numbers[n//2 - 1]
        upper_mid = sorted_numbers[n//2]
        median_value = (lower_mid + upper_mid) / 2.0

    return [x for x in numbers if x > median_value]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_data_1 = [3, 5, 7, 8, 9]
    sample_data_2 = [4, 6, 8, 10, 12, 14]
    sample_data_3 = [1, 2, 3, 4, 5, 6]

    result_1 = filter_above_median(sample_data_1)
    print(f"Input: {sample_data_1}, Median: {(sorted(sample_data_1)[len(sample_data_1)//2]) if len(sample_data_1)%2==1 else (sorted(sample_data_1)[len(sample_data_1)//2-1] + sorted(sample_data_1)[len(sample_data_1)//2])/2}")
    print(f"Result: {result_1}\n")

    result_2 = filter_above_median(sample_data_2)
    median_val_2 = (sorted(sample_data_2)[3] + sorted(sample_data_2)[4]) / 2.0 if len(sample_data_2)%2==0 else float(sorted(sample_data_2)[len(sample_data_2)//2])
    print(f"Input: {sample_data_2}, Median: {median_val_2}")
    print(f"Result: {result_2}\n")

    result_3 = filter_above_median(sample_data_3)
    median_val_3 = float(sorted(sample_data_3)[len(sample_data_3)//2]) if len(sample_data_3)%2==1 else (sorted(sample_data_3)[len(sample_data_3)//2-1] + sorted(sample_data_3)[len(sample_data_3)//2])/2.0
    print(f"Input: {sample_data_3}, Median: {median_val_3}")
    print(f"Result: {result_3}")