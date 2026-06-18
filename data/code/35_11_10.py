def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a given string,
    case-insensitive, ignoring all other characters efficiently.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel occurrences.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access
    samples = [
        "",                          # Empty string
        "hello world",               # Contains 2 vowels (e, o)
        "AEIOU123!",                 # All uppercase + non-alphabetic chars
        "rhythm",                    # No vowels in standard alphabet context here if ignoring y
        "aeiouyAEOIU",               # Includes 'y' which is not counted based on strict vowel definition used below (a,e,i,o,u only)
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"Input: '{sample}' -> Vowel Count: {result}")