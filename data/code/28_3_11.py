def compare_with_threshold(elements: list[float], threshold: float) -> bool:
    """Generator function that yields True if an element is larger than a fixed threshold."""
    for item in elements:
        yield item > threshold

if __name__ == '__main__':
    sample_list = [10, 25, 30.5, 45, 60]
    target_threshold = 20
    
    results = compare_with_threshold(sample_list, target_threshold)
    
    print("Comparison Results:")
    for is_greater in results:
        if is_greater:
            print(f"True")
        else:
            print(False)