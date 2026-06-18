def capitalize_sentence(sentence: str) -> str:
    """
    Capitalizes each word in a sentence, ensuring only the first letter 
    of each word is uppercase while preserving case sensitivity within words? 
    No - standard title casing (first char upper, rest lower).
    
    Args:
        sentence (str): The input string to process.
        
    Returns:
        str: A new string with each word's initial letter capitalized.
    """
    return " ".join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world, this is a test."
    result = capitalize_sentence(sample_sentence)
    print(result)