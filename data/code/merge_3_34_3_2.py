def capitalize_sentence(sentence: str) -> str:
    """
    Capitalize the first letter of each word in a sentence using list comprehension.
    
    Args:
        sentence (str): The input string to process.
        
    Returns:
        str: A new string with only the initial letter of each word capitalized,
             while preserving case for subsequent letters and original spacing.
    """
    return " ".join(word.capitalize() if len(word) > 1 else "".join(word[i].upper() + word[i+1:].lower()) 
                    for i, word in enumerate(sentence.split()))

if __name__ == '__main__':
    sample_sentence = "hello world this is a test sentence"
    result = capitalize_sentence(sample_sentence)
    print(result)