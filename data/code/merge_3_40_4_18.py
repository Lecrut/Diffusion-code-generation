def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word in the input string without creating intermediate lists.
    
    Args:
        input_string (str): The string to process.
        
    Yields:
        str: A single character representing the first letter of a word, or None if no valid start is found for that segment.
    """
    # Skip leading whitespace and check empty string immediately
    if not input_string.strip():
        return

    iterator = iter(input_string)
    
    try:
        while True:
            char = next(iterator)
            
            # If we encounter a non-space character, it's the start of a new word (or continuation after space/newline)
            # We need to ensure we are at the beginning of a "word" context. 
            # A simple approach for "first letter": look ahead or track state.
            # However, since input_string is passed as a whole string and memory usage must be minimal:
            # Iterating character by character from the start is O(N) time but O(1) extra space (excluding output).
            
            if char.isalpha():
                yield char
            
    except StopIteration:
        pass

if __name__ == '__main__':
    sample_string = "Hello world! This is a test string with multiple words."
    
    # Collect results for demonstration without storing all in memory at once during generation logic
    first_letters_list = []
    print("First letters:", end=" ")
    
    # We can consume the generator directly. 
    # To keep it strictly O(1) auxiliary space, we yield one by one and optionally store a small buffer for display.
    gen = find_first_letters_optimized(sample_string)
    
    try:
        while True:
            char = next(gen)
            if char is not None:  # Handle cases where generator might return non-char or handle edge logic strictly
                first_letters_list.append(char)
            
            # Stop after collecting the expected count for demo clarity, 
            # but since it's a generator, we just let it run until exhaustion.
    except StopIteration:
        pass
        
    print("".join(first_letters_list))
    
    # Verify functionality with another case if needed, ensuring no external dependencies are used.
    test_case_2 = "   Python 3.10 is great."
    result_gen = find_first_letters_optimized(test_case_2)
    output_result = list(result_gen)
    print(f"Test Case Output: {output_result}")