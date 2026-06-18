def capitalize_sentence(sentence: str) -> str:
    """
    Processes a sentence to ensure only the initial letter of each word is capitalized,
    preserving case for subsequent letters within words and handling punctuation correctly.
    
    Args:
        sentence (str): The input string representing a sentence or text block.
        
    Returns:
        str: A new string with proper capitalization applied to the first letter of each word.
    """
    # Split the sentence into words, keeping potential whitespace separation info is not needed here
    # We iterate through tokens defined by non-alphanumeric separators but we need a smarter split 
    # that respects punctuation attached to letters vs standalone punctuation at start/end
    
    # Strategy: Use regex-like logic via list comprehension and string slicing manually for portability without imports beyond standard lib
    words = []
    current_word_chars = []
    
    i = 0
    while i < len(sentence):
        char = sentence[i]
        
        if (char.isalpha() or char.isspace()):
            # If it's a space, handle the word we've been building
            if current_word_chars:
                words.append("".join(current_word_chars))
                current_word_chars = []
            i += 1
        elif not ('A' <= char < 'Z') and ('a' <= char < 'z'):
             # It's a non-alphabetic character (like punctuation) that is part of the word structure in this simplified approach? 
             # Actually, standard "capitalize" usually implies treating sequences like "hello." as one unit where '.' stays attached or treated separately.
             # The prompt asks for initial letter capitalization per word. In Python's str.capitalize() behavior: 'hElLo.' -> 'Hello.', but strict rules vary.
             # Let's assume standard definition: split by whitespace, capitalize each token if it contains letters? 
             # Or better yet, use the built-in logic adapted via list comp as requested constraint implies avoiding complex regex imports if possible but re is fine in stdlib.
             pass
        
        else:
            i += 1
            
    # Simpler approach using standard library tools wrapped in a generator expression for efficiency and conciseness
    
def capitalize_words(words):
    """Generator that capitalizes the first letter of each word."""
    for w in words:
        if not w.strip(): continue
        s = list(w)

if __name__ == '__main__':
    pass
