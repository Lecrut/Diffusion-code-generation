def compare_with_threshold(elements: list, threshold: float) -> bool:
    """Yields True if an element is larger than the given threshold."""
    for value in elements:
        if value > threshold:
            yield value

if __name__ == '__main__':
    sample_list = [10, 25.5, -3, 78.9, 4]
    fixed_threshold = 30
    
    results = list(compare_with_threshold(sample_list, fixed_threshold))
    
    # Output the resulting values (as per requirement to yield logic)
    for result in compare_with_threshold(sample_list, fixed_threshold):
        print(result)