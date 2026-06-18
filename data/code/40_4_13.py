def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word in the input string.
    
    This function processes the input string by splitting it into words 
    and yielding the first character (lowercase) of each non-empty word.
    It is designed to be memory efficient as a generator, processing items one at a time.

    Args:
        input_string (str): The string containing words separated by whitespace or punctuation.

    Yields:
        str: A single lowercase letter representing the first character of each found word.
    
    Example:
        >>> list(find_first_letters_optimized("Hello World"))
        ['h', 'w']
    """
    # Split the string into words based on whitespace and non-alphabetic characters as potential boundaries,
    # but we specifically look for sequences of alphabetic characters to define a "word".
    import re
    
    # Use regex to find all contiguous runs of letters. This handles punctuation attached to words correctly.
    matches = re.findall(r'[a-zA-Z]+', input_string)
    
    if not matches:
        return

    for word in matches:
        yield word[0].lower()

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid any need for user input or external resources.
    test_cases = [
        "The quick brown fox jumps over the lazy dog",
        "Hello, World! How are you today?",
        "Python is amazing and easy to learn.",
        "",  # Edge case: empty string
        "...!!!???"  # No letters present
    ]

    for test_input in test_cases:
        result = list(find_first_letters_optimized(test_input))
        print(f"Input: '{test_input}'")
        print(f"Output: {result}")
        print("-" * 30)