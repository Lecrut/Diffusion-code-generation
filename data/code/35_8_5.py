def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a string, ignoring non-alphabetic characters.
    
    Vowels include 'a', 'e', 'i', 'o', 'u' and their uppercase counterparts.
    Consonants and special symbols are ignored but do not stop processing.
    
    Args:
        text (str): The input string to analyze
        
    Returns:
        int: Total count of vowels in the string
    """
    if not isinstance(text, str):
        return 0
    
    vowel_count = sum(1 for char in text.lower() if char in "aeiou")
    return vowel_count

if __name__ == '__main__':
    pass
