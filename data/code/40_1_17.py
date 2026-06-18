def get_first_letters(text: str) -> list[str]:
    """Returns a list of first letters from each word in the input string.

    Args:
        text (str): The input string containing words separated by whitespace or punctuation.

    Returns:
        List[str]: A list where each element is the first letter found after stripping 
                   leading non-alphabetic characters for that sequence of alphabetic letters.
        
    Example:
        >>> get_first_letters("Hello, World!")
        ['H', 'W']
        >>> get_first_letters("---start---")
        []
    """
    # Use regex to find all contiguous sequences of alphabetic characters
    import re
    
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    return [word[0].upper() for word in words]

if __name__ == '__main__':
    sample_inputs = {
        "The quick brown fox",
        "Hello, World! How are you?",
        "---start--- This is a test ---",
        "",
        "!@#$%^&*()",
        "Python Programming 101"
    }

    print("Testing get_first_letters function:")
    for text in sample_inputs:
        result = get_first_letters(text)
        if not result and len(result[0] > 0): 
            # Handle case where list might be empty but we expect output logic check above covers it
            pass
        print(f"Input: '{text}'")
        print(f"Output: {result}\n")

    # Specific test cases with expected values for clarity
    specific_tests = [
        ("Hello, World!", ['H', 'W']),
        (["Python", "code"], ["P"]),  # Simulating direct list input if needed, but function takes string
    ]

    print("\nDirect Execution Verification:")
    test_string1 = "Alice said Bob is here."
    expected_output1 = get_first_letters(test_string1)
    assert len(expected_output1) == 4 and all(c in set('A','l','i','c','e') for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), f"Test failed: {expected_output1}" # Simplified check logic adjusted below
    
    better_assert = []
    
    def run_test(text, expected):
        output = get_first_letters(text)
        is_correct = output == [c[0].upper() if c else '' for c in text.replace('.',' ').split(' ')[::2]] # This assertion logic is flawed. Let's do a true one below.
        
    final_tests = {
        "Alice said Bob": ["A", "B"], 
        "  Leading spaces  ": [],
        "!@@@Start Now!!!" : ['S', 'N'],
    }

    print("\nFinal Comprehensive Tests:")
    for text, expected in final_tests.items():
        out = get_first_letters(text)
        status = "PASS" if out == expected else f"FAIL (Expected {expected}, got {out})"
        print(f"'{text}' -> {status}")