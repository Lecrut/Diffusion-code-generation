def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string, case-insensitive.
    
    The function ignores any non-alphabetic characters and only counts 
    standard English vowels ('a', 'e', 'i', 'o', 'u').
    
    Args:
        text (str): Input string to analyze.
        
    Returns:
        int: Total count of vowel characters in the input.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    vowels = set('aeiouAEIOU')
    
    # Using generator expression for memory efficiency with large strings
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "Python Programming",
        "aeiouAEIOU",
        "",
        "NoVowelsHere"
    ]

    print("Testing count_vowels function:")
    for s in sample_strings:
        result = count_vowels(s)
        print(f'Input: "{s}" -> Count: {result}')