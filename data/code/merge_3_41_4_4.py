import sys

def process_string(text: str) -> tuple[str, str, str]:
    """
    Takes a string input and returns three processed versions:
    1. The original string (stripped of leading/trailing whitespace).
    2. The fully capitalized version.
    3. The title case version (first letter of every word capitalized).

    Args:
        text (str): The input string to process.

    Returns:
        tuple[str, str, str]: A tuple containing the original, uppercased, and titled strings.
    """
    # Strip whitespace from both ends for consistent processing
    stripped_text = text.strip()
    
    # Fully capitalized version
    fully_capitalized = stripped_text.upper()
    
    # Title case version (first letter of every word)
    title_case = stripped_text.title()

if __name__ == '__main__':
    pass
