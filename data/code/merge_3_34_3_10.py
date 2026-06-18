def process_sentence(sentence: str) -> str:
    """
    Process a sentence to ensure only the initial letter of each word is capitalized.
    
    Args:
        sentence (str): The input string containing words separated by whitespace.
        
    Returns:
        str: A new string with proper capitalization for the first letter of each word.
    """
    # Use a generator expression to capitalize the first character and join parts back together
    return ' '.join(word.capitalize() if len(word) > 0 else '' 
                    for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world this is python programming"
    result = process_sentence(sample_sentence)
    print(result)