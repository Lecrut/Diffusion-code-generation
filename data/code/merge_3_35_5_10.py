def count_vowels(s: str) -> int:
    """
    Counts the occurrences of vowels in a string efficiently by iterating once.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        int: Total number of vowel characters found.
    """
    # Define set of vowels for O(1) lookup time
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    count = 0
    
    # Iterate through the string exactly once, checking each character against the vowel set
    for char in s:
        if char.lower() in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_strings = [
        "Hello, World!",           # Expected: e, o -> 2
        "AEIOUaeiou",              # Expected: all 10 letters are vowels -> 10
        "",                        # Expected: empty string -> 0
        "Python Programming",      # Expected: y is not vowel here (strict a,e,i,o,u) -> e, o -> 2
    ]

    for test_str in test_strings:
        result = count_vowels(test_str)
        print(f"String: '{test_str}'")
        print(f"Vowel Count: {result}")