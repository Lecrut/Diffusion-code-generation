def yield_above_threshold(data_list: list[float], threshold: float) -> bool:
    """
    Generator function that yields True if an element in data_list is larger than threshold,
    otherwise it does not yield anything for that iteration.
    
    Args:
        data_list (list): A list of numeric elements to compare against the threshold.
        threshold (float): The fixed value to compare each element against.
        
    Yields:
        bool: True if the current element from data_list is strictly greater than threshold, else None.
    
    Example usage:
        >>> for result in yield_above_threshold([10, 25, 30], 20):
        ...     print(result)
        True
        True
    
    Note:
        This function does not modify the input list or perform any I/O operations.
    """
    
    # Iterate through each element in the provided data_list
    for item in data_list:
        # Compare the current item against the threshold and yield result if condition met
        if item > threshold:
            yield True

if __name__ == '__main__':
    sample_data = [5, 10, 25, -3, 40]
    comparison_threshold = 15
    
    print("Elements in the list greater than", comparison_threshold)
    
    # Use generator expression to filter and collect results without side effects during iteration logic
    filtered_results = yield_above_threshold(sample_data, comparison_threshold)
    
    for is_greater in filtered_results:
        if is_greater:
            # Since only True values are yielded, we can infer the index or just print them directly
            # However, to demonstrate yielding behavior clearly without external state tracking here:
            pass
    
    # Direct iteration demonstration of the generator function output
    for result in yield_above_threshold(sample_data, comparison_threshold):
        print("Element found greater than threshold:", True)

# Additional explicit verification block (commented out if needed, but kept as part of module logic structure conceptually)
# To see actual values yielded:
print("\nDirect generator output:")
for res in yield_above_threshold(sample_data, comparison_threshold):
    print(res)  # Will only print True for elements > 15