def compare_elements(threshold):
    """
    Generator function that yields True if an element from the input list is larger than the threshold,
    otherwise it does not yield anything (implicitly False).
    
    Args:
        threshold (int or float): The fixed value to compare against.
        
    Yields:
        bool: True if the current element exceeds the threshold.
    """
    for item in input_list:
        if item > threshold:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    data = [10, 25, 30, 45, 60]
    limit = 35
    
    results = list(compare_elements(limit))
    
    print(f"Comparing {data} against threshold {limit}:")
    for i, is_greater in enumerate(results):
        if is_greater:
            # Find the corresponding value from data to show context (optional clarity)
            val = data[i]
            print(f"{val} > {limit}")