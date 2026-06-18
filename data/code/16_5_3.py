def positive_generator(iterable):
    """
    Generator function that yields True for every positive number encountered in an input iterable.
    
    Args:
        iterable (iterable): An iterable containing numbers to check.
        
    Yields:
        bool: True if the current element is a positive number, otherwise does not yield anything.
    """
    for item in iterable:
        # Check if the item is an instance of int or float and greater than 0
        if isinstance(item, (int, float)) and item > 0:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values to test the generator without user input
    sample_data = [1, -5, 3.5, "not a number", 2, 0, 4]
    
    print("Testing positive_generator with:", end=" ")
    print(sample_data)
    
    results = list(positive_generator(sample_data))
    
    # Display the yielded values (all should be True for valid positives)
    if results:
        print(f"Yielded {len(results)} times:")
        for i, result in enumerate(results):
            original_item = sample_data[i]
            is_positive = isinstance(original_item, (int, float)) and original_item > 0
            status = "True" if result else "Not yielded"
            print(f"Item {original_item} ({type(original_item).__name__}): Expected positive? {is_positive}, Generator: {status}")
    else:
        print("No positive numbers found.")