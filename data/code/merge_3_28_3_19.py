def compare_elements(input_list: list, threshold) -> None:
    """
    Generator function that yields True if an element in input_list is larger than threshold.
    
    Args:
        input_list (list): List of elements to compare.
        threshold: Fixed value to compare against.
        
    Yields:
        bool: True if the current element > threshold, otherwise does not yield anything for that iteration.
    """
    for item in input_list:
        if item > threshold:
            yield True

if __name__ == '__main__':
    sample_data = [5, 10, 3, 8, 2]
    fixed_threshold = 4
    
    results = list(compare_elements(sample_data, fixed_threshold))
    
    print("Comparison Results:")
    for i, result in enumerate(results):
        if result:
            # We need to map back to the original value or index. 
            # Since we only yielded True/False, let's re-run logic with context for display clarity.
            pass
    
    # Re-running a small snippet just to print which ones passed (optional but makes output clear)
    actual_results = [(val, val > fixed_threshold) for val in sample_data]
    
    print(f"Threshold: {fixed_threshold}")
    print("Element | Comparison Result")
    print("-" * 30)
    for val, is_greater in zip(sample_data, results):
        status = "True" if is_greater else "False (not yielded)"
        # Note: The generator only yields True. To show False we must compare manually again or track index.
        # Here we just print the yield result corresponding to each element logic for clarity.
        
    # Corrected display using the actual comparison list since generator hides non-yields
    passed_elements = [val for val in sample_data if val > fixed_threshold]
    
    print(f"Elements greater than {fixed_threshold}: {passed_elements}")