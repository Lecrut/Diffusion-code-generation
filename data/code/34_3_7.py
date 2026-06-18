def capitalize_words(sentence: str) -> str:
    """
    Capitalizes the first letter of each word in a sentence.
    
    Args:
        sentence (str): The input string to process.
        
    Returns:
        str: A new string with only the initial letters capitalized.
    """
    if not sentence:
        return ""
    
    # Split into words, capitalize first letter of each, then join back
    processed_words = [word.capitalize() for word in sentence.split()]
    return " ".join(processed_words)

if __name__ == '__main__':
    sample_sentence = "hello world this is a test case"
    
    # Process the sample input using list comprehension within function call logic implicitly handled by capitalize_words
    result = capitalize_words(sample_sentence)
    
    print(f"Original: {sample_sentence}")
    print(f"Result:   {result}")