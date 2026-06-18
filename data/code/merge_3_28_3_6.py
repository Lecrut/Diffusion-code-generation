def compare_elements(data_list: list, threshold) -> None:
    """
    Generator function that yields True if an element in data_list is greater than threshold.
    
    Args:
        data_list (list): The input list of elements to check.
        threshold: The fixed value to compare each element against.
        
    Yields:
        bool: True if the current element > threshold, otherwise does not yield anything for that iteration.
    """
    for item in data_list:
        if item > threshold:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_data = [5, 10, 3, 8, 2]
    fixed_threshold = 4
    
    results = list(compare_elements(sample_data, fixed_threshold))
    
    print("Comparison Results:")
    for i, result in enumerate(results):
        if result:
            # We can't easily map back to original index without tracking it internally or modifying the generator logic slightly.
            # To keep it simple and strictly following "yields True when element > threshold", 
            # we will print a message indicating which elements passed, but since generators don't naturally expose indices unless tracked:
            pass
    
    # Let's refactor slightly to show context in output without changing the core generator logic requested.
    # We'll iterate again with index tracking for demonstration purposes only (not part of yield).
    
    print(f"\nChecking elements against threshold {fixed_threshold}:")
    count = 0
    passed_count = sum(results) if results else 0
    
    # Re-iterate to show which ones were yielded True, since the generator itself doesn't return indices.
    for item in sample_data:
        is_greater = (item > fixed_threshold)
        print(f"Element {item}: {'> Threshold' if is_greater else '<= Threshold'}")
    
    # Demonstrate the actual yield behavior by re-running or just confirming logic via results list above
    # Since we already computed 'results', let's verify it matches expectations.
    expected_results = [x > fixed_threshold for x in sample_data]
    
    print(f"\nExpected boolean sequence: {expected_results}")
    print(f"Actual yielded values (sum/count): {passed_count} out of {len(sample_data)}")