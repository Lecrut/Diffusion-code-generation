def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a string, 
    regardless of case.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "aeiouAEIOU123"
    ]

    for test_string in samples:
        count = count_vowels(test_string)
        print(f"'{test_string}' contains {count} vowel(s).")