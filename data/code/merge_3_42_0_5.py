"""
Module to concatenate a list of strings with a specified delimiter.

This script defines a function that takes an iterable of strings and a 
delimiter string, returning their concatenation separated by the delimiter.
It includes a main execution block with hard-coded sample values for testing.
No user input or external dependencies are required.
"""

def concatenate_strings(input_list: list[str], separator: str) -> str:
    """
    Concatenates all strings in the provided list into a single string, 
    separated by the specified delimiter.

    Args:
        input_list (list): A list of strings to be concatenated.
        separator (str): The string used as a delimiter between items.

    Returns:
        str: The resulting concatenated string. If the list is empty, 
             returns an empty string without adding separators.
    
    Example:
        >>> concatenate_strings(["Hello", "World"], ", ")
        'Hello, World'
        
        >>> concatenate_strings([], "-")
        ''
    """
    if not input_list:
        return ""
    result = [str(item) for item in input_list]
    return separator.join(result)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user interaction, network access, or file I/O is performed here.
    
    sample_data_1 = ["Python", "is", "awesome"]
    delimiter_one = ", "
    
    sample_data_2 = ["The quick brown fox", "jumps over the lazy dog"]
    delimiter_two = "\n"
    
    # Test case 1: Default separator logic
    output_1 = concatenate_strings(sample_data_1, delimiter_one)
    
    # Test case 2: Newline separator and multiple lines
    output_2 = concatenate_strings(sample_data_2, delimiter_two)
    
    print("Sample Output 1:")
    print(output_1)
    
    print("\nSample Output 2:")
    print(output_2)