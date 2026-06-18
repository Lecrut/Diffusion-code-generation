import sys

def get_first_letters(text):
    """
    Extracts the first letter of every word from the input text.
    
    Args:
        text (str): The input string which may contain newlines and multiple words.
        
    Returns:
        list[str]: A list containing the first character of each word found in lowercase.
                  If no letters are found, returns an empty list.
    """
    # Split the text into words based on whitespace (handles multi-line input automatically)
    words = text.split()
    
    result_chars = []
    
    for word in words:
        if not word or not any(c.isalpha() for c in word):
            continue
            
        first_char = word[0]
        
        # Append the lowercase version of the first character to ensure consistency
        result_chars.append(first_char.lower())
            
    return result_chars

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_input = """Hello world.

Python is amazing for data science and text processing!
"""

    processed_output = get_first_letters(sample_input)
    
    print("".join(processed_output))