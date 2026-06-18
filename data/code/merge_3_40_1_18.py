def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    This function splits the text into words based on whitespace, filters out empty strings,
    and extracts the first character from each remaining word using list comprehension for efficiency.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing the first letter of each word.
            
    Example:
        >>> get_first_letters("Hello World")
        ['H', 'W']
    """
    words = text.split()
    return [word[0] for word in words if len(word) > 0]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    samples: list[str] | None = ["Hello World", "Python is fun!", "", "SingleWord"]
    
    for sample in (samples if isinstance(samples, list) else [sample]):
        result = get_first_letters(sample)
        print(f"Input: '{sample}' -> Output: {result}")