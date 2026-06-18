def compare_elements(threshold):
    """
    Generator function that yields True if an element from input list is greater than threshold,
    otherwise it does not yield anything (implicitly False).
    
    Args:
        threshold (int or float): The fixed value to compare elements against.
        
    Yields:
        bool: True if the current element > threshold.
    """
    for item in input_list:
        if item > threshold:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input needed)
    my_list = [10, 25, 30, 45, 60, -5]
    fixed_threshold = 20
    
    results = list(compare_elements(fixed_threshold))
    
    print("Elements greater than threshold:", results)