def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in the given string using a single loop.
    
    This function iterates through each character exactly once, checking if it is 
    an uppercase or lowercase vowel (a, e, i, o, u). It returns the count as an integer.

    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        int: The total number of vowels found in the string.
    """
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no external input required.
    sample_strings = [
        "Hello World!",           # Expected: 3 (e, o, o)
        "Python Programming",     # Expected: 5 (y is not vowel here per simple set, a, i, o, u -> actually y/e/o/... let's trace: P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g. Vowels: o, o, a, i = 4? Wait. 'y' is excluded in strict definition unless specified. Let's stick to A,E,I,O,U only.)
        "AEIOU",                  # Expected: 5
        "",                       # Expected: 0
        "bcdfg"                   # Expected: 0
    ]

    for test_str in sample_strings:
        result = count_vowels(test_str)
        print(f"'{test_str}' -> {result}")