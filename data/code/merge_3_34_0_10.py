import re

def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Use regex to find all words in the string and capitalize their first letters.
    # \b matches word boundaries (transitions between word characters [\w] and non-word characters).
    capitalized_words = re.findall(r'\b(\w)\w*', text)
    
    if not capitalized_words:
        return text

    result_parts = []
    for match in capitalized_words:
        first_char = match[0].upper()
        rest_of_word = match[1:]
        # Preserve the original casing of the remaining characters by joining them back.
        word_result = f"{first_char}{rest_of_word}"
        result_parts.append(word_result)

    return ''.join(result_parts)

if __name__ == '__main__':
    sample_text = "hello world! this is a test string."
    
    # Process the hard-coded sample value directly without any user input.
    output_string = capitalize_words(sample_text)
    
    print(f"Input:  {sample_text}")
    print(f"Output: {output_string}")