def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a string, ignoring non-alphabetic characters.
    
    Vowels considered: 'a', 'e', 'i', 'o', 'u' (case-insensitive).
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        int: Total count of vowels in the text.
    """
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    
    for char in text.lower():
        if char.isalpha() and char in vowel_set:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    samples = [
        "Hello, World!",
        "aeiouAEIOU",
        "Python3.9 is great! No numbers here.",
        "",
        "!@#$%^&*()"
    ]

    for s in samples:
        result = count_vowels(s)
        print(f"Input: '{s}' -> Vowel Count: {result}")