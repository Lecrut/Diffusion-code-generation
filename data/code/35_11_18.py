def count_vowels(text: str) -> int:
    """
    Returns an integer representing the total count of vowels in the input string.
    
    This function is optimized to handle strings efficiently by avoiding 
    repeated character lookups through a set membership test that operates on lowercase characters,
    then adjusting for uppercase matches using ASCII value checks or direct iteration with conditional logic.
    Non-alphabetic characters are ignored without raising errors.

    Parameters:
        text (str): The input string to analyze.

    Returns:
        int: Total count of vowels ('a', 'e', 'i', 'o', 'u' case-insensitive).
    
    Complexity Analysis:
        Time: O(n) where n is the length of the string, as each character is processed exactly once.
        Space: O(1), using a fixed set for vowel characters regardless of input size.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    count = 0
    
    # Iterate through the string and check each character's lowercase form against our vowel set
    char_lower = text.lower()
    for ch in char_lower:
        if ch in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    test_cases = [
        "Hello, World!",           # Expected: 2 (e, o)
        "AEIOU",                   # Expected: 5
        "",                        # Expected: 0
        "Programming is fun.",     # Expected: 3 (o, i, u)
        "12345 @#$%^&*()",         # Expected: 0
    ]

    for test_string in test_cases:
        result = count_vowels(test_string)
        print(f"Input: '{test_string}' -> Vowel Count: {result}")