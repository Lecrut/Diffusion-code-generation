def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a string, ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowel occurrences.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    sample_text = "Hello, World! 1234567890"
    result = count_vowels(sample_text)
    print(result)