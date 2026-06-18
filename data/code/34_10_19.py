def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    samples = [
        "hello world",
        "python is awesome!",
        "this   has   multiple  spaces",
        "no change here",
        ""
    ]

    for test_input in samples:
        result = capitalize_words(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{result}'\n")