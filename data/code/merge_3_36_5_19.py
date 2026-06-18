def reverse_string_generator(s: str):
    """
    Generator function that yields characters of an input string in reverse order.
    
    Optimizes memory usage by avoiding slicing which creates a copy, 
    instead using Python's native negative indexing on the original string 
    (which is optimized internally) or iterating backwards from index -1 to 0.

    Args:
        s (str): The input string to iterate over in reverse order.
    
    Yields:
        str: One character at a time, starting from the last character of the string
             and moving towards the first.
    """
    # Iterating backwards from -1 down to 0 avoids creating intermediate lists or strings,
    # which is crucial for memory efficiency with very large input data compared to 
    # methods like reversed(list(s)) that convert the entire string to a list first.
    for i in range(-1, -(len(s) + 1), -1):
        yield s[i]

if __name__ == '__main__':
    sample_string = "HelloWorld"
    
    # Demonstrate usage of the generator without consuming it entirely immediately
    reverse_chars = reverse_string_generator(sample_string)
    
    print("Reversed characters:")
    for char in reverse_chars:
        print(char, end='')
    
    print()  # Newline at the end
    
    # Verify with a larger string to simulate potential memory constraints context
    large_sample = "A" * 10**6 + "Z"
    large_gen = reverse_string_generator(large_sample)
    
    last_char_from_large = next(large_gen)
    print(f"\nFirst character yielded from very large string: {last_char_from_large}") # Should be 'Z'
    
    remaining_count = len(sample_string) + 10**6 - 1
    count = sum(1 for _ in reverse_chars if True) 
    # Note: The above loop reuses the exhausted iterator variable logic conceptually, 
    # but strictly speaking we need a fresh generator or re-run to verify full yield.

    # Corrected verification block using a fresh generator instance
    gen2 = reverse_string_generator("TestString")
    
    result_list = []
    for char in gen2:
        result_list.append(char)
    
    print(f"\nGenerated list from 'TestString': {result_list}")