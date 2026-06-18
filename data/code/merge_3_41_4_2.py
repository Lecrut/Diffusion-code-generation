import sys

def process_string(text: str) -> tuple[str, str, str]:
    """
    Processes a string to return three variations:
    1. The original string.
    2. Fully capitalized version (upper()).
    3. Title case version (first letter of every word capitalized).

    Args:
        text (str): Input string.

    Returns:
        tuple[str, str, str]: A tuple containing the three processed strings.
    """
    original = text
    fully_capitalized = text.upper()
    
    # Handle empty string or whitespace-only case for title logic safely
    if not original.strip():
        capitalized_words = ""
    else:
        # Using str.title() handles multiple spaces and non-alphabetic characters correctly per Python docs
        capitalized_words = original.title()

    return (original, fully_capitalized, capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    
    result_original, result_uppercase, result_titlecased = process_string(sample_input)
    
    print(result_original)
    print(result_uppercase)
    print(result_titlecased)