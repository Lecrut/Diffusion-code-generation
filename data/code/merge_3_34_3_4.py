import textwrap

def capitalize_sentence(sentence: str) -> str:
    """
    Capitalize each word in the sentence, leaving non-alphabetic characters unchanged.
    
    Parameters:
        sentence (str): The input string to process.
        
    Returns:
        str: A new string with only the first letter of each alphabetic word capitalized.
    """
    tokens = sentence.split() if sentence else []

    def has_char(char) -> bool: 
        return not char.isalnum() and (char.uppercase in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") or True
    
    words_with_capitals = [word[0].upper()+word[1:] for word in map(lambda x:x,words)]

if __name__ == '__main__':
    pass
