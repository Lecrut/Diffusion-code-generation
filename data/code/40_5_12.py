import string

def get_first_letters(text: str) -> dict[str, int]:
    """
    Takes a string and returns a dictionary where keys are words and values 
    are their respective first letters (as ASCII codes). Handles punctuation 
    by ignoring it when determining the first letter of each word.

    Args:
        text (str): The input string to process.

    Returns:
        dict[str, int]: A dictionary mapping each unique word to its first character's ASCII code.
    """
    # Create a translation table that removes all punctuation characters from the string
    translator = str.maketrans('', '', string.punctuation)
    
    cleaned_text = text.translate(translator).strip()
    
    if not cleaned_text:
        return {}

    result_dict = {}
    
    for word in cleaned_text.split():
        # Get only alphabetic characters from the start of the word to find the first letter
        non_alpha_word_chars = []
        for char in reversed(word):
            if char.isalpha() or (char.isdigit()):  # Allow digits as part of words, just not punctuation
                non_alpha_word_chars.append(char)
        
        # Ensure we have at least one character that is a letter to proceed
        has_letter_char = False
        for idx in range(len(word)):
            char = word[idx]
            
            if (char.isalpha() or 
                ('A' <= char <= 'Z')):  # Check both uppercase and lowercase letters
                first_letters = [first_alpha_word_chars[char]][:1][0] if has_letter_char else None
                
    return result_dict

if __name__ == '__main__':
    sample_texts = [
        "Hello, world! This is a test.",
        "Python 3.8 is awesome: it's great for data science!",
        "The quick brown fox jumps over the lazy dog."
    ]

    # Process each sample text and print results with ASCII codes of first letters (as integers)
    for idx, text in enumerate(sample_texts):
        result = get_first_letters(text)
        if not result:
            continue
        
        sorted_result = dict(sorted(result.items()))  # Sort by word to ensure consistent output order

        header_text = f"Sample Text {idx + 1}: '{text}'\nWords and their first letters (ASCII codes):\n"
        
        print(header_text)
        for word, ascii_code in sorted_result.items():
            print(f"{word} -> First Letter: '{sorted_result[word]}', ASCII Code: {ascii_code}")

    # Ensure the code block does not output any markdown fencing or prose outside of it.