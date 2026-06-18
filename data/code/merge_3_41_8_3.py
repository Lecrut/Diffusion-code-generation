def format_string(text: str) -> str:
    """
    Creates a formatted string containing three versions of the input text:
    1. The original text.
    2. All-caps version.
    3. Sentence-case version (first letter capitalized, rest lowercase).

    Args:
        text (str): The input string to be processed.

    Returns:
        str: A comma-separated string of the three formatted versions.
    """
    original = text
    
    # Built-in method for all-caps conversion
    caps_version = original.upper()
    
    # Sentence-case logic using slicing and built-ins
    if not original:
        sentence_case = ""
    else:
        first_char = original[0].upper()
        rest_chars = "".join([char.lower() for char in original[1:]])
        sentence_case = f"{first_char}{rest_chars}"

    return f"{original}, {caps_version}, {sentence_case}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    samples = ["Hello World", "Python Programming", ""]
    
    for test_input in samples:
        result = format_string(test_input)
        print(f"Input: '{test_input}'")
        print(result)
        print("---")