import sys

def capitalize_first_letter(text):
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized,
             preserving original casing for subsequent characters and non-alphabetic prefixes if any.
    """
    words = text.split()
    result_words = []
    
    for word in words:
        # Handle empty strings or purely numeric/symbolic start cases gracefully by checking length
        if not word:
            continue
            
        first_char = word[0]
        
        # Check if the character is alphabetic to decide capitalization logic
        if 'a' <= first_char <= 'z':
            new_first_char = chr(ord(first_char) - 32)
            rest_of_word = word[1:]
            result_words.append(new_first_char + rest_of_word)
        else:
            # If not alphabetic, keep as is (e.g., numbers or symbols remain unchanged at start)
            result_words.append(word)
            
    return ' '.join(result_words)

if __name__ == '__main__':
    sample_inputs = [
        "hello world",
        "python programming language",
        "the quick brown fox jumps over the lazy dog"
    ]
    
    for input_text in sample_inputs:
        output_text = capitalize_first_letter(input_text)
        print(f"Input: '{input_text}'")
        print(f"Output: '{output_text}'\n")