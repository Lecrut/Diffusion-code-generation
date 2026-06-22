from typing import Tuple

MAX_RECURSION_DEPTH = 10000
DELIMITER = " "

def extract_boundary_words(text: str) -> Tuple[str, str]:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    if len(text) == 0:
        raise ValueError("Input string cannot be empty")
        
    words = text.split(DELIMITER)
    
    clean_words = [word for word in words if word]
    
    if not clean_words:
        raise ValueError("Input string contains no valid words")
        
    first_word = clean_words[0]
    last_word = clean_words[-1]
    
    return first_word, last_word

if __name__ == '__main__':
    sample_data = "   Leading spaces   middle   words   trailing   "
    first, last = extract_boundary_words(sample_data)
    print(first)
    print(last)