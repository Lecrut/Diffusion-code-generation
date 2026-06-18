import string

def yield_non_whitespace(s: str):
    """
    Generator function that yields characters from an input string, skipping whitespace.

    Args:
        s (str): The input string to process.

    Yields:
        str: Single character items found in the input string that are not whitespace.
    """
    for char in s:
        if char.strip():  # Checks if the character is not a space, tab, newline, etc.
            yield char

if __name__ == '__main__':
    sample_string = "Hello World! This is Python."
    
    print("Original string:", sample_string)
    result_list = list(yield_non_whitespace(sample_string))
    output_str = ''.join(result_list)
    
    print("Filtered characters:", ', '.join(char for char in result_list))
    print("Joined non-whitespace string:", output_str)