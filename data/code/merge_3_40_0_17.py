import re

def get_first_letters(text: str) -> list[str]:
    """
    Extracts the first letter of each word from the input string.
    
    Handles various whitespace scenarios (spaces, tabs, newlines, multiple spaces).
    Ignores non-alphabetic characters when determining a 'word' start if necessary,
    but primarily relies on standard word boundaries for simplicity and robustness.
    If no words are found or the input is empty/only punctuation/symbols without letters,
    returns an empty list.

    Args:
        text (str): The input string to process.

    Returns:
        list[str]: A list containing the first letter of each word in lowercase.
                   If a word contains no alphabetic characters, it is skipped.
    """
    # Split by any whitespace sequence using regex for robustness against tabs/newlines/multiple spaces
    words = re.split(r'\s+', text.strip())

    result = []
    
    for word in words:
        if not word:  # Skip empty strings resulting from split on leading/trailing separators (though strip handles this)
            continue
            
        # Find the first alphabetic character in the word
        match = re.search(r'[a-zA-Z]', word)
        
        if match:
            result.append(match.group(0).lower())

    return result

if __name__ == '__main__':
    sample_inputs = [
        "Hello World",
        "\t\tPython\nis\nawesome!",
        "   Multiple      spaces  here. ",
        "---No letters---",
        "123Numbers456OnlySymbols!!!",
        "MixedCase: CamelCase and snake_case"
    ]

    for sample in sample_inputs:
        output = get_first_letters(sample)
        print(f"Input: {repr(sample)}")
        print(f"Output: {output}")
        print("-" * 30)