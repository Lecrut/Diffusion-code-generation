def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a given string.
    
    The function is case-insensitive and ignores any characters that are not vowels.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found in the string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Define vowels for case-insensitive matching using set lookup for efficiency
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    count = 0
    
    # Iterate through each character in the input text
    for char in text:
        if char.lower() in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or external dependencies.
    samples = [
        "Hello, World!",
        "AEIOUaeiou",
        "Python programming is fun.",
        "",
        "xyz"
    ]

    for test_string in samples:
        result = count_vowels(test_string)
        print(f"'{test_string}' -> {result}")