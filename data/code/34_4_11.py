import sys

def capitalize_first_letter(text):
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first character of each word capitalized,
             while preserving case for all other characters and original spacing structure.
    """
    words = text.split()
    result_words = []
    
    # Handle empty input explicitly before splitting
    if not words:
        return ""

    for i in range(len(words)):
        current_word = words[i]
        
        # Check if the word has at least one character to avoid index errors or unintended capitalization
        if len(current_word) > 0 and 'a' <= current_word[0].lower() <= 'z':
            capitalized_char = current_word[:1].upper()[0:1] + current_word[1:]
            
            # If the first letter was already uppercase, keep it as is (no change needed), 
            # but we must ensure we don't accidentally lowercase a second character if input is weird.
            # The requirement says "only capitalize", implying others stay same case.
            result_words.append(capitalized_char + current_word[1:])

        else:
            # If the first letter isn't in 'a'-'z', just return it as is to avoid breaking logic on numbers/symbols at start
            result_words.append(current_word)

    return " ".join(result_words)

if __name__ == '__main__':
    sample_input = "hello world, this is a test string."
    
    # Process the hard-coded sample value directly without any user input prompts or arguments.
    output_text = capitalize_first_letter(sample_input)
    
    print(output_text)