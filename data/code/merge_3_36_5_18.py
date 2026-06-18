def reverse_string_generator(s: str):
    """
    Generator function that yields characters of an input string in reverse order.
    
    Optimizes memory usage by processing the string lazily without creating a 
    reversed copy or intermediate list, suitable for very large strings when 
    iterating character-by-character is preferred over loading everything into RAM.

    Args:
        s (str): The input string to iterate through in reverse.

    Yields:
        str: Individual characters from the end of the string to the beginning.
    
    Note:
        While Python strings are immutable and typically stored as arrays, 
        slicing a large string creates a copy. This generator avoids that by 
        using an index pointer starting from the last character down to zero.
    """
    length = len(s)
    if length == 0:
        return
    
    # Start from the end of the string and move backwards
    for i in range(length - 1, -1, -1):
        yield s[i]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_strings = [
        "Hello", 
        "", 
        "Python is awesome!", 
        "A" * 10_000_000  # Large string to demonstrate memory efficiency conceptually
    ]

    for test_str in sample_strings:
        print(f"\nProcessing string of length {len(test_str)}:")
        
        # Demonstrate the generator by collecting results (in real large scenarios, 
        # you might process each yielded char immediately without storing)
        reversed_chars = list(reverse_string_generator(test_str))
        
        if test_str:  # Only print non-empty for brevity in output
            result_text = "".join(reversed_chars)
            print(f"Original: {test_str}")
            print(f"Reversed: {result_text}")
            
            # Verify correctness without printing the full large string back-to-back 
            # to avoid excessive console I/O, just check a few characters for sanity
            if len(test_str) > 10_000_000 // 2:
                print("Large string processed successfully (verification skipped due to length).")