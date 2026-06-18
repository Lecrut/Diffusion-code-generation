def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a sentence.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    words = text.split()
    return " ".join(word.capitalize() for word in words)

if __name__ == '__main__':
    sample_sentence = "hello world this is a test sentence"
    result = capitalize_words(sample_sentence)
    print(result)