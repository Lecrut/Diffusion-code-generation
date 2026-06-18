def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in the given string, including both lowercase 
    and uppercase letters ('a', 'e', 'i', 'o', 'u'). Non-alphabetic characters are ignored.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels in the string.
    """
    vowel_set = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowel_set)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_strings = [
        "Hello, World!",      # Expected: 2 ('e', 'o')
        "AEIOUaeiou",         # Expected: 10 (all characters are vowels)
        "Python3.8 is great!","Expected: 4 ('a', 'y' is not a vowel here in this strict definition, but let's stick to standard AEIOU only -> actually Python has no vowels? Wait: P-y-t-h-o-n-3-. -i-s- -g-r-e-a-t-!. Vowels: o, i, e, a. So 4.",
        "123!@#",             # Expected: 0 (no vowels)
        "",                   # Expected: 0 (empty string)
    ]

    for s in sample_strings:
        print(f"Input: {s!r} -> Vowel Count: {count_vowels(s)}")