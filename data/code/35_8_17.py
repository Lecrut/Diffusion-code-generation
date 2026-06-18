def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a string, ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowel occurrences.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_cases = [
        "Hello, World!",  # Expected: 2 (e, o)
        "aeiou",          # Expected: 5
        "1234!@#",       # Expected: 0
        "Python Programming",  # Expected: 6 (y is not counted here based on strict vowel definition; a,e,o,i,u -> P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g. Vowels: o, o, a, i = 4? Let's re-evaluate strictly.)
        # Re-checking "Python Programming": 
        # p (no), y (strictly no in this context unless specified as vowel, but standard is aeiouAEIOU), t(no), h(no), o(yes), n(no) -> 1 so far.
        # space(ignore), P(no), r(no), o(yes), g(no), r(no), a(yes), m(no), m(no), i(yes), n(no), g(no).
        # Total: o, o, a, i = 4. 
    ]

    results = []
    for test_input in test_cases:
        count = count_vowels(test_input)
        results.append(f"Input: '{test_input}' -> Count: {count}")

    print("\n".join(results))