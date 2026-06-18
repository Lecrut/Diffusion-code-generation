import re

def capitalize_first_letter(text: str) -> str:
    """
    Processes a block of text to apply the rule where only the first letter 
    of every word is capitalized, preserving the original casing and spacing 
    structure as much as possible while ensuring standard capitalization rules.
    
    This implementation uses regular expressions to identify words (sequences 
    of alphanumeric characters) and applies title case transformation strictly 
    to each identified word without affecting punctuation or numbers within them,
    except for their initial letter which is converted to uppercase if alphabetic.

    Args:
        text (str): The input string containing the block of text to process.

    Returns:
        str: A new string with only the first letter of each word capitalized.

    Example:
        >>> capitalize_first_letter("hello world, this is a test.")
        "Hello World, This Is A Test."
        >>> capitalize_first_letter("  multiple   spaces here ")
        ' Multiple Spaces Here'
    """
    if not text or not isinstance(text, str):
        return ""

    # Pattern matches sequences of alphanumeric characters (words)
    words = re.findall(r'\b\w+\b', text)
    
    result_parts = []
    for word in words:
        # Capitalize only the first character if it is alphabetic, keep rest as is
        capitalized_word = ''
        char_list = list(word)
        length = len(char_list)
        
        i = 0
        while i < length:
            current_char = char_list[i]
            if current_char.isalpha():
                # Capitalize only the first letter of the word found by regex
                if i == 0:
                    capitalized_word += current_char.upper()
                else:
                    capitalized_word += current_char.lower() 
                break
            
            elif not current_char.isdigit() and not any(c >= 'a' <= c < 'z' for c in [current_char]): # Check unicode letter roughly but safe fallback logic below is better via translation or direct check. Let's simplify using string methods on the slice.
                 i += 1

if __name__ == '__main__':
    pass
