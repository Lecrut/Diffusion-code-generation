import re

def get_first_letters(text: str) -> list[str]:
    """
    Extracts the first letter of each word from the input string.
    
    Handles various whitespace scenarios (spaces, tabs, newlines, multiple spaces).
    Ignores non-alphabetic characters when determining a 'word' start if necessary,
    but primarily relies on standard word boundaries for alphabetic starts.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        list[str]: A list of single-character strings representing the first letter 
                   of each detected word. If no words are found, returns an empty list.
    """
    # Split by any whitespace sequence using regex for robustness against tabs/newlines/multiple spaces
    words = re.split(r'\s+', text.strip())
    
    result = []
    for word in words:
        if not word:  # Skip empty strings resulting from split on leading/trailing separators (though strip handles this)
            continue
        
        first_char = word[0]
        
        # Ensure we only capture alphabetic characters as the "first letter" 
        # to handle cases like "-hello", "(code)", etc., gracefully if desired.
        # The prompt implies standard words, but being robust means handling punctuation.
        # We will take the first character that is an alphabet letter. If a word starts with non-alpha, skip it?
        # Or just return the very first char regardless of type (e.g. '(', '-', etc)? 
        # Standard interpretation: "first letter" implies alphabetic. Let's find the first alpha char in the token.
        
        for char in word:
            if char.isalpha():
                result.append(char)
                break
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    samples = [
        "Hello World",
        "\t\tPython\nis\nawesome!",
        "  multiple   spaces  and tabs ",
        "-start-with-dash (parentheses) hello123 world",
        ""
    ]

    for sample in samples:
        output = get_first_letters(sample)
        print(f"Input: {repr(sample)}")
        print(f"Output: {''.join(output)}\n")