def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string using a single loop.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters ('a', 'e', 'i', 'o', 'u') found in the string, 
             regardless of case.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "aeiouAEIOU",
        "xyz"
    ]

    for test_string in samples:
        result = count_vowels(test_string)
        print(f"'{test_string}' -> {result}")