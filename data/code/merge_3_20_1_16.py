def case_insensitive_equal(s1: str, s2: str) -> bool:
    """Check if two strings are equal in a case-insensitive manner."""
    return s1.lower() == s2.lower()

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or network access.
    samples = [
        ("Hello", "hello"),       # Should be True (case differs)
        ("HELLO WORLD!", "hElLo WoRLd!"),  # Should be True (mixed case with punctuation/spaces preserved)
        ("Test123", "test456"),   # Should be False (different characters despite same length and case-insensitive match on letters)
        ("", ""),                  # Should be True (empty strings are equal)
    ]

    for i, (str_a, str_b) in enumerate(samples):
        result = case_insensitive_equal(str_a, str_b)
        print(f"Test {i + 1}: '{str_a}' == '{str_b}' is {result}")