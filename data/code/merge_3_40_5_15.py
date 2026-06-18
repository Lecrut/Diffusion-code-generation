def get_first_letters(word_string):
    """
    Takes a string input and returns a dictionary where keys are words 
    and values are their respective first letters, handling punctuation correctly by ignoring it.
    
    Args:
        word_string (str): The input string containing words with potential punctuation.
        
    Returns:
        dict: A dictionary mapping each unique word to its lowercase first letter.
    """
    # Split the string into tokens based on whitespace and other non-alphanumeric separators
    # We use a regex approach conceptually but standard split handles most cases; 
    # however, for strict punctuation removal before checking words, we'll process carefully.
    
    result_dict = {}
    
    # Replace all non-alphabetic characters with spaces to isolate words effectively?
    # Or better: iterate through the string and identify word boundaries properly.
    # Let's assume standard definition of a word is contiguous alphanumeric sequence (and optionally underscores).
    # We will clean punctuation by removing it temporarily or skipping it when finding first char.
    
    current_word = ""
    
    for index, character in enumerate(word_string):
        if character.isalnum() and not character.startswith('_'): 
            # Include letters, digits, but typically words are just letters here based on "first letter" requirement.
            # Let's strictly take alphabetic characters as part of the word to determine 'the first letter'.
            current_word += character
        
    # Since simple split might include attached punctuation (e.g., "hello,"), 
    # we need a robust way to extract words and their leading letters ignoring surrounding punctuation.
    
    import re
    
    # Extract all sequences of alphanumeric characters as potential words
    found_words = re.findall(r'\b\w+\b', word_string)
    
    for word in found_words:
        if not word: 
            continue
            
        first_char = word[0]
        
        # Ensure we only care about alphabetic starting letters? The prompt says "first letter".
        # Usually implies [a-zA-Z]. If a word starts with a digit, it's technically the first character.
        # However, in natural language processing contexts for this type of task, 
        # 'letter' usually means an alphabet letter. Let's assume standard lowercase conversion is expected.
        
        if not (first_char.isalpha()):
            continue
            
        lower_first = first_char.lower()
        
        result_dict[word] = lower_first
        
    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "Hello, world! This is a test.",
        "Python 3.9: Great language for data science!",
        "One two three four five",
        "123 numbers start with digits but we ignore them as per 'letter' logic if strictly alphabetic required." # Adjusted based on interpretation of 'first letter'. If digit allowed, keep it. Let's assume strict alphabet for safety or just take char[0]. 
    ]

    print("Sample Output:")
    for test_input in test_cases:
        output = get_first_letters(test_input)
        print(f"Input: '{test_input}'")
        print(output)
        
        # Verify specific expected behavior manually for one case if needed, but let's trust the logic.
        # "Hello," -> {"hello": "h"} (assuming word extraction strips punctuation first via regex \b\w+\b handles non-word chars as delimiters effectively? 
        # Actually re.findall(r'\b\w+\b', ...) splits on non-alphanumeric/non-underscore boundaries automatically for this pattern.
        
    print("\nAdditional detailed check:")
    sample = "Hello, World! How are you?"
    output_sample = get_first_letters(sample)
    print(f"Input: '{sample}'")
    # Expected logic trace: 
    # Words found by \b\w+\b on "Hello, World! How are you?": ["hello", "world", "how", "are", "you"] (case preserved in findall usually unless specified)
    # First letters: h -> 'h', w -> 'w', h -> 'h' (key exists so overwrite or keep unique?), a -> 'a', y -> 'y'. 
    # The prompt says keys are words. Usually implies uniqueness of key is fine if same word appears twice, but here we iterate once per found sequence.
    
    print(output_sample)