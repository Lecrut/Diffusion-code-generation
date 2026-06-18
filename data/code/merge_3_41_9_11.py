def case_swap(text: str) -> dict[str, str]:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' to their respective 
    case transformations of the input string. Prioritizes readability and performance 
    by using built-in Python methods which are optimized in CPython.

    Args:
        text (str): The input string to transform.

    Returns:
        dict[str, str]: A dictionary with keys 'lower', 'upper', and 'title'.
    """
    lower_text = text.lower()
    upper_text = text.upper()
    
    # Construct title case by capitalizing the first letter of each word 
    # while keeping the rest lowercase. This is more efficient than manual slicing 
    # for most cases as it leverages existing optimized string methods, though strictly 
    # Python's built-in str.title() does not handle edge cases like apostrophes in "don't" 
    # perfectly (it lowercases them). For a robust title case that preserves internal capitalization
    # if desired, one might implement custom logic, but the task asks for standard transformations.
    # We will use the built-in str.title() as it is readable and performant for general cases.
    title_text = text.title()

    return {
        'lower': lower_text,
        'upper': upper_text,
        'title': title_text
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    samples = [
        "hello world",
        "HELLO WORLD",
        "Python Programming 101!",
        "",
        "a b c d e"
    ]

    for sample in samples:
        result = case_swap(sample)
        print(f"\nInput: '{sample}'")
        print("Lower:", repr(result['lower']))
        print("Upper:", repr(result['upper']))
        print("Title:", repr(result['title']))