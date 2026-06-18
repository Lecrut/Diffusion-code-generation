def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string using a single loop.
    
    Vowels considered include 'a', 'e', 'i', 'o', 'u' and their uppercase counterparts.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels in the string.
    """
    vowel_set = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowel_set)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [
        "hello world",      # Expected: 2 (e, o)
        "AEIOU",            # Expected: 5
        "rhythm",           # Expected: 0
        "aeiou AEIOU aeiou",# Expected: 13
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"'{sample}' -> {result}")