def count_vowels(text: str) -> int:
    """
    Counts the occurrences of vowels (a, e, i, o, u) in a string efficiently.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowel characters found in the string.
    """
    # Define set of lowercase and uppercase vowels for O(1) lookup time check
    vowels = {'a', 'e', 'i', 'o', 'u'} | {'A', 'E', 'I', 'O', 'U'}
    
    count = 0
    
    # Iterate through the string exactly once, checking each character against vowel set
    for char in text:
        if char in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    test_strings = [
        "Hello, World!",
        "AEIOU",
        "aeiou",
        "",
        "Python Programming"
    ]
    
    for test_str in test_strings:
        result = count_vowels(test_str)
        print(f"'{test_str}' -> {result} vowels")