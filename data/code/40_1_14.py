def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list where each element is the first character of a word found in the text.
                   Words are defined as sequences of alphanumeric characters separated by non-alphanumeric boundaries.
    """
    words = text.split()
    return [word[0].lower() if len(word) > 1 else (word.lower(),)[0] for word in words]

if __name__ == '__main__':
    sample_text = "Hello World! Python Programming is Fun."
    result = get_first_letters(sample_text)
    print(result)