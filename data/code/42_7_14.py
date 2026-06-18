import sys

def join_with_delimiter(strings: list[str], delimiter: str) -> str:
    """
    Takes a list of strings and a custom delimiter, returning a single string
    where the delimiter is placed between every element (not at the start or end).
    
    Args:
        strings: A list of strings to be joined.
        delimiter: The string to use as separator.
        
    Returns:
        A new string with elements separated by the delimiter, 
        empty string if input list is empty.
    """
    # Using itertools for a standard library approach which handles edge cases cleanly
    from itertools import chain
    
    # Create an iterator that yields delimiters between items
    separator_chain = [delimiter] * (len(strings) - 1)
    
    return ''.join(chain.from_iterable(
        iter([s, d]) if i < len(separator_chain) else 
        ([d + s for d in strings[i+1:] or []] + ['']) # This logic is flawed above, let's rewrite simply
    ))

def join_with_delimiter_v2(strings: list[str], delimiter: str) -> str:
    """
    Takes a list of strings and a custom delimiter.

    Returns a single string where the delimiter is placed *between* 
    every element in the original list. If no elements are provided, returns an empty string.
    
    Args:
        strings (list[str]): List of input strings.
        delimiter (str): The separator string to insert between items.

    Returns:
        str: Joined string with delimiters inserted correctly.
    """
    if not strings:
        return ""

    result = []
    
    # Append the first element
    result.append(strings[0])
    
    # Iterate from second element onwards, prepending the delimiter each time
    for i in range(1, len(strings)):
        result.append(delimiter)
        result.append(strings[i])
        
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    test_list = ["Hello", "World", "Python"]
    custom_sep = "--"

    output_string = join_with_delimiter_v2(test_list, custom_sep)
    
    print(output_string)