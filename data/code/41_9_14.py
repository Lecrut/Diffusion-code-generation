def case_swap(text: str) -> dict[str, str]:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' to their 
    respective case transformations of the input string.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
              - 'lower': All characters converted to lowercase.
              - 'upper': All characters converted to uppercase.
              - 'title': First letter of each word capitalized, rest lowercased.
    
    Performance Note: Uses built-in string methods which are implemented 
    in C for optimal speed and readability.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    result = {
        'lower': text.lower(),
        'upper': text.upper(),
        'title': text.title()
    }
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "hello world",
        "PYTHON IS GREAT",
        "Mixed CASE 123",
        ""
    ]

    for text in samples:
        transformed = case_swap(text)
        print(f"Input: '{text}'")
        print("Lower:", repr(transformed['lower']))
        print("Upper:", repr(transformed['upper']))
        print("Title:", repr(transformed['title']))
        print("-" * 20)