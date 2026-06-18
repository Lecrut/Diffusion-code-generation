def format_string(text: str) -> str:
    """
    Creates a formatted string containing three versions of the input text:
    1. The original text.
    2. All uppercase version.
    3. Sentence case version (first letter capitalized, rest lowercase).

    Args:
        text (str): The input string to process.

    Returns:
        str: A comma-separated string of the three formatted versions.
    """
    original = text
    
    # Use built-in method for all-caps conversion
    upper_case = text.upper()
    
    # Create sentence case using slicing and replace
    if len(text) > 0:
        first_char = text[0].capitalize()
        rest_chars = text[1:].lower()
        sentence_case = first_char + rest_chars
    else:
        sentence_case = ""

    return f"{original}, {upper_case}, {sentence_case}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files
    samples = [
        "hello world",
        "Python is awesome!",
        "   leading spaces  ",
        ""
    ]

    for sample in samples:
        result = format_string(sample)
        print(result)