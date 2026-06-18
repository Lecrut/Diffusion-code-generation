def compare_elements(data_list: list, threshold) -> bool:
    """
    Generator function that yields True if an element in data_list is greater than threshold, False otherwise.
    
    Args:
        data_list (list): The input list of elements to check.
        threshold: The fixed value to compare each element against.
        
    Yields:
        bool: True if the current element > threshold, else False.
    """
    for item in data_list:
        yield item > threshold

if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    fixed_threshold = 20
    
    results = compare_elements(sample_data, fixed_threshold)
    
    print("Comparison Results:")
    for result in results:
        if result is True:
            # We can't access the original value here easily without a wrapper generator, 
            # but per task requirements we just yield the boolean comparison.
            pass
        
        # To demonstrate usage clearly while adhering to strict output rules:
        print(f"Element > {fixed_threshold}: {result}")