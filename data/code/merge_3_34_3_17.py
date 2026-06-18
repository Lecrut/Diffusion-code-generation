def capitalize_words(sentence: str) -> str:
    """
    Capitalize the first letter of each word in a sentence using list comprehension.
    
    Args:
        sentence (str): The input string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world, this is a test."
    result = capitalize_words(sample_sentence)
    print(result)