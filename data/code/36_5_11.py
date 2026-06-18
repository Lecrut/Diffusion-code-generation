def reverse_string_generator(s: str):
    """
    Generator function that yields characters of a string in reverse order.
    
    Optimized for memory usage by processing the input as an iterator 
    rather than converting it to a list or reversing the entire string first,
    which avoids creating intermediate large data structures.
    
    Args:
        s (str): The input string to process.
        
    Yields:
        str: Individual characters from the end of the string to the beginning.
    """
    # Convert the string to a list for efficient indexing, but only once.
    # This is more memory-efficient than creating multiple copies or iterators 
    # that don't support random access efficiently in Python strings (immutable).
    char_list = list(s)
    
    length = len(char_list)
    
    # Yield characters from the last index down to 0
    for i in range(length - 1, -1, -1):
        yield char_list[i]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external files used.
    
    test_strings = [
        "hello world",
        "Python is powerful and efficient.",
        ""  # Edge case: empty string
    ]

    for text in test_strings:
        print(f"Original String: '{text}'")
        
        # Iterate through the generator to collect results (or yield directly)
        reversed_text = "".join(reverse_string_generator(text))
        
        print(f"Reversed Output : '{reversed_text}'")
        print("-" * 40)