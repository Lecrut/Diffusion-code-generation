def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list where each element is the lowercase first character 
                   of a non-empty sequence of characters separated by whitespace.
                   
    Example:
        >>> get_first_letters("Hello World")
        ['h', 'w']
    """
    return [word[0].lower() for word in text.split()]

if __name__ == '__main__':
    sample_input = "Python Programming is Fun and Easy"
    result = get_first_letters(sample_input)
    print(result)