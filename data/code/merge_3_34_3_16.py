def capitalize_sentence(sentence: str) -> str:
    """
    Capitalizes the first letter of each word in a sentence.
    
    Args:
        sentence (str): The input string to process.
        
    Returns:
        str: A new string with each word's first character capitalized and words separated by spaces.
             Words are defined as sequences of alphanumeric characters ignoring punctuation at the start/end unless part of an acronym.
             For simplicity in this idiom, we split on whitespace and capitalize the first char of resulting tokens if they have length > 0.
    """
    return " ".join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world! python is awesome."
    result = capitalize_sentence(sample_sentence)
    print(result)