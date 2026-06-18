def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string using a single loop.
    
    Vowels considered include 'a', 'e', 'i', 'o', 'u' and their uppercase equivalents.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels in the string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    test_cases = [
        "Hello, World!",
        "AEIOU",
        "",
        "rhythm",
        "aeiouaEiOu"
    ]

    for case in test_cases:
        result = count_vowels(case)
        print(f"'{case}' -> {result}")