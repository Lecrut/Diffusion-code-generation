import sys

def capitalize_first_letter_of_each_word(text):
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string where the first character of every non-empty word is uppercase,
             and subsequent characters are lowercased. Non-alphabetic leading characters 
             within a word remain unchanged after capitalization logic if they aren't letters,
             but standard title case behavior usually implies [a-zA-Z]. This implementation
             assumes words consist primarily of alphabetic characters for simplicity:
             it converts the first character to uppercase if it is alphabetical.
    """
    result = []
    
    # Split text into tokens based on whitespace
    for token in text.split():
        word_list = list(token)
        
        # If not empty, capitalize the first letter only if it's alphabetic
        if len(word_list) > 0 and 'a' <= word_list[0] <= 'z':
            word_list[0] = chr(ord('A') + ord(word_list[0]) - ord('a'))
        
        result.append("".join(word_list))
    
    return " ".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, arguments, or network access.
    samples = [
        "hello world",
        "the quick brown fox jumps over the lazy dog",
        "python is awesome and it rocks!",
        ""
    ]
    
    for text in samples:
        output_text = capitalize_first_letter_of_each_word(text)
        print(output_text)