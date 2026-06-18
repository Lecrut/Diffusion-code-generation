def compare_elements(data_list: list, threshold) -> None:
    """
    Generator function that yields True if an element in data_list is greater than threshold.
    
    Args:
        data_list (list): The input list of elements to check.
        threshold: The fixed value against which each element is compared.
        
    Yields:
        bool: True if the current element > threshold, otherwise does not yield anything for that iteration.
    """
    for item in data_list:
        if item > threshold:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_data = [10, 25, -3, 40.5, 7]
    fixed_threshold = 15

    results = list(compare_elements(sample_data, fixed_threshold))
    
    print("Comparison Results:")
    for i, result in enumerate(results):
        if result:
            # We can't easily map back to original index without tracking, 
            # but the task only asks for yielding True/False logic.
            pass
    
    # Demonstrate the generator by printing which items passed (optional clarity)
    print(f"Threshold used: {fixed_threshold}")
    print("Items greater than threshold:")
    
    count = 0
    current_idx = 0
    temp_gen = compare_elements(sample_data, fixed_threshold)
    for item in sample_data:
        if next(temp_gen):
            print(f"Index {current_idx}: Value {item}")
            count += 1
    
    print(f"\nTotal items greater than threshold: {count}")