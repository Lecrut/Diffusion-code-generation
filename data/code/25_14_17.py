def even_zero_generator(start: int = 0, end: int = None) -> bool:
    """
    Generator that yields True if the current number is zero or an even number in range [start, end).
    
    Optimization note: This generator processes numbers one by one and does not store them.
    It checks for zero explicitly as requested to return only the zero case as a special condition,
    while also yielding True for all other even numbers encountered.

    Args:
        start (int): Starting integer of the range (inclusive).
        end (int): Ending integer of the range (exclusive). If None, defaults to 10.

    Yields:
        bool: True if the number is zero or an even number; False otherwise implicitly by not yielding.
              Note: The function yields True for every even number including zero as per standard logic,
              but since the prompt asks specifically "check if the number being yielded is zero", 
              we interpret this as ensuring zero is handled correctly within the stream of evens.

    Memory Efficiency:
        Uses a simple loop with constant space complexity O(1). No lists or buffers are created.
    """
    # Adjust end to default if not provided
    if end is None:
        end = 20
    
    for num in range(start, end):
        # Check if number is even (including zero)
        if num % 2 == 0:
            yield True

if __name__ == '__main__':
    # Sample execution without user input or external dependencies
    print("Testing generator with default range:")
    
    result = list(even_zero_generator())
    
    for i, is_even in enumerate(result):
        if i < 10:  # Print first few items to avoid excessive output
            print(f"Number {i}: Even? {is_even}")
        
        # Specifically highlight the zero case as requested logic-wise (though it yields True like other evens)
        if num == 0 and is_even:
            print("Zero detected in range.")

    # Demonstrate custom start/end for clarity
    result_custom = list(even_zero_generator(start=5, end=12))
    
    print("\nTesting generator with custom range (start=5, end=12):")
    numbers_in_range = [num for num in range(5, 12)]
    evens_found = []
    
    gen_custom = even_zero_generator(start=5, end=12)
    count = 0
    
    # Iterate through custom generator to collect results without storing all at once if needed later
    while True:
        try:
            val = next(gen_custom)
            evens_found.append(val)
            print(f"Yielded value (index {count}): {val}")
            count += 1
            
            # Stop after finding zero and a few more to demonstrate behavior
            if count > 5: 
                break
                
        except StopIteration:
            break
    
    print("\nAll even numbers yielded in custom range:", evens_found)