def count_vowels(text):
    """
    Counts the total number of vowels (a, e, i, o, u) in a given string,
    ignoring case sensitivity.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found in the string.
    """
    # Define vowels as lowercase for consistency; comparison will be done via .lower() or set lookup
    return sum(1 for char in text if char.lower() in "aeiou")

if __name__ == '__main__':
    pass
