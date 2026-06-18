def count_vowels(text: str) -> int:
    """Counts the total number of vowels (a, e, i, o, u) in a string, case-insensitive."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_cases = [
        "Hello, World!",           # Expected: 2 (e, o)
        "AEIOU",                   # Expected: 5
        "Python Programming",      # Expected: 4 (y is not counted here based on strict definition; a, i, o are vowels -> actually 'o' only? Let's re-verify. Python has y,o,r,g,a,m,m,i,n-g. Vowels in this context usually include Y but task says a,e,i,o,u strictly.)
        # Re-evaluating "Python Programming": P-y-t-h-o-n (y no, o yes) P-r-o-g-r-a-m-m-i-n-g (o,yes; a,yes; i,yes). Total: 1+3 = 4. Correct.
        "",                        # Expected: 0
    ]

    for test_string in test_cases:
        result = count_vowels(test_string)
        print(f"Input: '{test_string}'")
        print(f"Vowel Count: {result}")