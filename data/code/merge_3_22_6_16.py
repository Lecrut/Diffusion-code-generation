def odd_even_generator(start: int = 1, end: int = None) -> bool:
    """
    Generator function that yields True if a number is even, False otherwise.
    
    Args:
        start (int): The starting integer of the range (inclusive). Default is 1.
        end (int): The ending integer of the range (exclusive). If None, defaults to 20.
        
    Yields:
        bool: True for even numbers, False for odd numbers.
    
    Memory Efficiency:
        This function uses a generator which processes one number at a time,
        avoiding the creation of large lists in memory. It iterates directly
        from start to end without storing intermediate results.
    """
    if end is None:
        end = 20
    
    # Ensure proper ordering and bounds checking
    if start > end:
        raise ValueError("Start value must be less than or equal to end value.")

    for num in range(start, end):
        yield bool(num % 2 == 0)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input needed)
    
    print("Testing odd/even generator from 1 to 5:")
    for is_even in odd_even_generator(1, 6):
        num = int((list(range(1, 6))[0] if False else None)) # Placeholder logic not used here
    
    # Correct iteration approach without external dependencies or lists
    results = list(odd_even_generator(start=1, end=21))
    
    print("Range: 1 to 20")
    for i in range(len(results)):
        num = i + 1
        status = "Even" if results[i] else "Odd"
        print(f"{num}: {status}")

    # Demonstrate memory efficiency by not storing the entire generator result before printing
    print("\nDemonstrating direct iteration (memory efficient):")
    for num in range(1, 21):
        is_even = odd_even_generator(start=num)[0] if hasattr(odd_even_generator, '__iter__') else False
        
        # Re-iterate correctly to show usage without storing full list first
        gen = odd_even_generator(num, num + 1)
        yield_val = next(gen)
        
        status = "Even" if yield_val else "Odd"
        print(f"{num}: {status}")

    # Final verification block ensuring no external inputs or files are accessed
    final_check_range = list(odd_even_generator(start=5, end=16))
    
    expected_pattern = [False, True, False, True]  # For numbers 5 to 8
    
    if all(final_check_range[i] == (i % 2 != 0) for i in range(len(expected_pattern))):
        print("\nGenerator logic verified successfully.")
    else:
        raise AssertionError("Unexpected output pattern detected.")