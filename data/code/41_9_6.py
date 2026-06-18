def case_swap(text: str) -> dict[str, str]:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' 
    to their respective case transformations of the input string.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
              - 'lower': All characters converted to lowercase.
              - 'upper': All characters converted to uppercase.
              - 'title': First letter of each word capitalized, rest lowercased.
    
    Performance Note: Uses built-in string methods which are implemented in C 
    for optimal performance and readability without external dependencies.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    return {
        'lower': text.lower(),
        'upper': text.upper(),
        'title': text.title()
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "hello world",
        "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",
        "Python 3.12 is awesome!",
        ""
    ]

    for sample in samples:
        result = case_swap(sample)
        print(f"Input: '{sample}'")
        print(f"Lower: {result['lower']}")
        print(f"Upper: {result['upper']}")
        print(f"Title: {result['title']}")
        print("-" * 30)