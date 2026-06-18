def reverse_string_generator(s):
    """
    Generator function that yields characters of an input string in reverse order.
    
    Optimizes memory usage by not creating a reversed copy or list first,
    but rather iterating backwards over the original string's indices directly.
    This approach works well for large strings as it only stores references to 
    individual character objects without duplicating the entire sequence.

    Args:
        s (str): The input string to be processed in reverse order.
        
    Yields:
        str: Single characters from the end of the string to the beginning.
    
    Example:
        >>> list(reverse_string_generator("hello"))
        ['o', 'l', 'l', 'e', 'h']
    """
    # Iterate backwards over indices using range with a negative step
    for index in range(len(s) - 1, -1, -1):
        yield s[index]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    
    test_strings = [
        "hello",              # Simple string
        "Python is great!",  # String with spaces and punctuation
        "1234567890"         # Numeric characters only
    ]

    for sample in test_strings:
        print(f"\nOriginal: {sample}")
        
        result = reverse_string_generator(sample)
        
        output_list = []
        for char in result:
            output_list.append(char)
        
        reversed_output_str = "".join(output_list)
        print(f"Reversed via generator: {reversed_output_str}")