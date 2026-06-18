def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string, 
    handling both uppercase and lowercase letters while ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: Total count of vowels ('a', 'e', 'i', 'o', 'u') in the string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    vowels = set('aeiouAEIOU')
    
    # Use generator expression for memory efficiency on large strings
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample_1 = "Hello, World!"
    sample_2 = "Programming is fun."
    sample_3 = ""
    
    results = [
        count_vowels(sample_1),
        count_vowels(sample_2),
        count_vowels(sample_3)
    ]
    
    print(f"Vowel count in '{sample_1}': {results[0]}")
    print(f"Vowel count in '{sample_2}': {results[1]}")
    print(f"Vowel count in empty string: {results[2]}")