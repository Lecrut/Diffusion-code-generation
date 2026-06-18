import re

def get_first_letter_of_each_word(text: str) -> list[str]:
    """
    Extracts the first letter of each word from the input string.
    
    Handles various whitespace scenarios (spaces, tabs, newlines, multiple spaces).
    Ignores non-alphabetic characters that might appear before a valid starting letter 
    if they are not part of the initial sequence intended as a 'word start' in this context.
    However, strictly following standard word definition: sequences separated by whitespace.
    
    If a word contains no alphabetic character, it is skipped to ensure we only print letters.
    
    Args:
        text (str): The input string containing words and various whitespaces.
        
    Returns:
        list[str]: A list of single-character strings representing the first letter 
                   of each valid word found in the input.
    """
    # Split by any whitespace sequence, which handles spaces, tabs, newlines efficiently
    raw_words = text.split()
    
    result_letters = []
    
    for word in raw_words:
        if not word:
            continue
            
        # Find the first alphabetic character in the word
        match = re.search(r'[a-zA-Z]', word)
        
        if match:
            result_letters.append(match.group(0))
            
    return result_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, stdin, or network access is needed.
    test_cases = [
        "Hello World",                          # Standard case with single spaces
        "  Python   Programming\nis fun.",     # Multiple spaces and newlines
        "\t\tTabbed words here.\nAnd more!",  # Tabs and mixed whitespace
        "NoAlpha123Chars456StartsHere",         # Words without leading letters (should skip non-alpha start)
    ]

    for test_input in test_cases:
        print(f"Input: {repr(test_input)}")
        output = get_first_letter_of_each_word(test_input)
        print("Output:", "".join(output))
        print("-" * 20)