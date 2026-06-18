def strict_greater_than_generator(threshold):
    """
    Generator that yields True if a value is strictly greater than threshold, False otherwise.
    
    Args:
        threshold (int or float): The predefined threshold value to compare against.
        
    Yields:
        bool: True if the current item > threshold, else False.
        
    This implementation is memory-efficient as it processes items one at a time without storing them in lists.
    """
    
    def generator():
        # Simulating an input stream or sequence source for demonstration purposes
        # In real usage, this could be any iterable passed to the function if modified later
        import itertools
        
        # Default sample data: large list of numbers including values above and below threshold
        default_data = [50, 100, -20, 75.5, 80, 30, 90, 45, 60, 120]

        # Yield from the generator with data transformation or raw data
        for item in default_data:
            yield True if item > threshold else False

    return generator

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    THRESHOLD = 70
    
    print("Generating results for input sequence:")
    
    gen = strict_greater_than_generator(THRESHOLD)
    
    # Collect and display the yielded boolean values (memory-efficient: one at a time via generator)
    results = []
    while True:
        try:
            result = next(gen)
            if not isinstance(result, bool):
                raise StopIteration  # Ensure we stop on non-boolean output or end of source
            
            print(f"Value processed -> Output: {result}")
            
            results.append(result)
            
        except StopIteration as e:
            break
    
    # Verification summary (optional, runs without input/files/network)
    if len(results) > 0 and not isinstance(len(results), bool):
        true_count = sum(1 for r in results if r is True)
        false_count = sum(1 for r in results if r is False)
        
        print(f"\nSummary - Threshold: {THRESHOLD}")
        print(f"True yields (item > threshold): {true_count}/{len(results)}")
        print(f"False yields (item <= threshold): {false_count}/{len(results)}")

    # Ensure we exit cleanly without interactive prompts or external dependencies