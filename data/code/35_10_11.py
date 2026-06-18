def count_vowels(text):
    """
    Counts the total number of vowels in a given string, case-insensitive.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels found in the string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert text to lowercase and iterate through each character
    return sum(1 for char in text.lower() if char in vowel_set)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "AEIOU",
        "",
        "Python programming is fun.",
        "bcdfg"
    ]

    for test_input in sample_strings:
        result = count_vowels(test_input)
        print(f'Input: "{test_input}"')
        print(f'Vowel Count: {result}')