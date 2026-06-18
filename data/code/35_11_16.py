def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string, 
    handling both uppercase and lowercase letters while ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters ('a', 'e', 'i', 'o', 'u' in any case).
    """
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        "Hello, World!",       # Expected: 3 (e, o, o)
        "AEIOUaeiou",          # Expected: 10
        "Rhythm is sweet!",   # Expected: 2 (i, e)
        "",                    # Expected: 0
        "Python programming"  # Expected: 4 (o, i, a, o)
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"'{sample}' -> {result} vowels")