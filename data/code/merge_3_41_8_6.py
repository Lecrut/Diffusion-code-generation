def format_string(text: str) -> str:
    """
    Creates a formatted string containing three versions of the input text:
    1. The original case version.
    2. All uppercase letters.
    3. Sentence-case (first letter capitalized, rest lowercase).

    Args:
        text (str): The input string to process.

    Returns:
        str: A comma-separated string of the three formatted versions.
    """
    original = text
    all_caps = text.upper()
    
    # Create sentence case by capitalizing only the first character if present, then lowercasing the rest
    if len(text) > 0:
        sentence_case = text[0].capitalize() + ''.join(c.lower() for c in text[1:])
    else:
        sentence_case = ""

    return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = format_string(sample_input)
    print(result)