def compare_elements(data_list: list, threshold) -> bool:
    """
    Generator function that yields True if an element in data_list is greater than threshold.
    
    Args:
        data_list (list): List of elements to be compared.
        threshold: The fixed value against which each element is compared.
        
    Yields:
        bool: True if the current element is larger than the threshold, otherwise False.
    """
    for item in data_list:
        yield item > threshold

if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    fixed_threshold = 20
    
    results = list(compare_elements(sample_data, fixed_threshold))
    
    print("Comparison Results:")
    for i, result in enumerate(results):
        element = sample_data[i]
        status = "Larger" if result else "Not Larger"
        print(f"{element}: {status}")