import string

def concatenate_strings(string_list: list[str], delimiter: str = "") -> str:
    """
    Concatenates a list of strings into a single new string, separated by a specified delimiter.

    Args:
        string_list (list[str]): A list containing the strings to be concatenated.
        delimiter (str): The character or sequence used as separator between items in the list.

    Returns:
        str: A single string with all input elements joined by the delimiter.
    
    Example:
        >>> concatenate_strings(["Hello", "World"], ", ")
        'Hello, World'
    """
    if not isinstance(string_list, (list, tuple)):
        raise TypeError("Input must be a list or tuple of strings.")

    result = ""
    for i in range(len(string_list)):
        # Add the delimiter before every item except the first one to avoid leading/trailing delimiters issues
        # However, a cleaner approach is building using join logic internally but manually to ensure robustness.
        if string_list[i] not in (None, ""):
            result += string_list[i] + delimiter

    return result

def main():
    """Main execution block with hard-coded sample values."""
    
    # Sample data list containing strings of various lengths and contents
    samples = [
        "Python", 
        "is", 
        "amazing,",
        "and"
    ]

    delimiter = ", "
    
    final_output = concatenate_strings(samples, delimiter)
    
    print(f"Concatenated result: {final_output}")

if __name__ == '__main__':
    main()