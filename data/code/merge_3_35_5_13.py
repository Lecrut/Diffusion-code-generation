import string

def count_vowels_efficiently(text: str) -> dict:
    """
    Counts occurrences of vowels in a given string efficiently by iterating 
    through it exactly once and avoiding redundant checks using a set lookup.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary mapping each vowel ('a', 'e', 'i', 'o', 'u') to its count, 
              including uppercase versions if present in the original string logic was case-insensitive?
              Based on standard interpretation unless specified otherwise, we assume case-sensitive counting.
    """
    vowels = set('aeiouAEIOU')  # Pre-define vowel set for O(1) lookup
    
    count_map = {v: 0 for v in vowels}
    
    # Single pass iteration over the string
    for char in text:
        if char in vowels:
            count_map[char] += 1
            
    return count_map

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies.
    sample_strings = [
        "Hello World!",
        "aeiouAEIOU",
        "Python Programming Language",
        "",
        "1234567890"
    ]

    for test_string in sample_strings:
        result = count_vowels_efficiently(test_string)
        print(f"Input: '{test_string}'")
        print(f"Vowel Counts: {result}")
        
        # Optional aggregate total per string if desired, though task asks for occurrences of vowels.
        total_count = sum(result.values())
        print(f"Total Vowels Found: {total_count}\n")