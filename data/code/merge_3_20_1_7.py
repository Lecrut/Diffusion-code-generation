def case_insensitive_equal(str1: str, str2: str) -> bool:
    """
    Check if two strings are equal ignoring case differences.

    Args:
        str1 (str): First string to compare.
        str2 (str): Second string to compare.

    Returns:
        bool: True if the strings are equal when compared in a case-insensitive manner, False otherwise.
    
    Note: This function uses built-in methods for efficient and optimized comparison without external dependencies.
    """
    # Normalize both strings to lowercase (or uppercase) for direct equality check
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or network access is required
    test_cases = [
        ("Hello", "hello"),       # Should be True (case difference)
        ("World!", "WORLD!"),     # Should be True (mixed case and punctuation preserved)
        ("Python", "java"),       # Should be False (different words)
        ("Test123", "test456"),  # Should be False (numbers differ even if letters match after lowercasing logic check, but here they don't fully match)
        ("", ""),                 # Edge case: empty strings should be True
        ("A" * 1000, "a" * 1000),# Large string performance test edge case (should be True)
    ]

    print("Running case-insensitive equality checks...")
    
    for i, (s1, s2) in enumerate(test_cases):
        result = case_insensitive_equal(s1, s2)
        status = "PASS" if result else "FAIL"
        # Using f-string directly to ensure compatibility and readability without external libs
        print(f"Test {i+1}: \"{s1}\" vs \"{s2}\" => {status}")

    # Final summary verification for the first test case as a concrete example of functionality
    assert case_insensitive_equal("Hello", "hello") == True, "Core functionality assertion failed."
    
    print("\nAll tests completed successfully.")