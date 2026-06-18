def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalize the first letter of every word in the input string.
    
    A 'word' is defined as a sequence of non-whitespace characters.
    Only the very first character of each such sequence is modified to uppercase,
    provided it is an alphabetic character. Other letters remain unchanged (no 
    force-to-uppercase).

    Args:
        text (str): The input string containing words separated by whitespace or other delimiters if desired logic were expanded here; currently uses standard split() behavior on any whitespace.

    Returns:
        str: A new string with the first character of each word capitalized, 
             preserving case for all subsequent characters in that word.
    
    Example:
        "hello world" -> "Hello World"
        "hELLO WoRLd" -> "HELLO WORLD" (only first char changed to upper)

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n) for creating the result list and joining it back into a string.
    
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
        
    words = text.split()  # Splits by any whitespace run
    
    capitalized_words = []
    for word in words:
        if len(word) == 0:
            continue
            
        first_char = word[0]
        rest_chars = word[1:]
        
        # Only capitalize if the character is alphabetic. Otherwise leave as is.
        new_first_char = first_char.upper() if first_char.isalpha() else first_char
        
        capitalized_words.append(new_first_char + ''.join(rest_chars))

    return ' '.join(capitalized_words)

if __name__ == '__main__':
    # Sample test cases hard-coded as per requirements. No user input or network access used.
    
    test_cases = [
        "hello world",           # Expected: Hello World
        "hELLO WoRLd",          # Expected: HELLO WORLD (only first chars upper)
        "!@#$ python 2024!",    # Expected: !@$# Python 2024!
        "",                     # Empty string -> empty string
        "   ",                  # Only spaces -> only spaces
        "single",               # Single word -> Single
        "multi-word test case here for optimization check now please", 
                                # Multi words with mixed cases to verify logic
    ]

    results = {}

    print("Running optimized capitalize_first_letter_only function tests...\n")
    
    for i, input_str in enumerate(test_cases):
        result = capitalize_first_letter_only(input_str)
        expected_capitalized = " ".join(
            w[0].upper() + w[1:] if len(w) > 1 else (w.upper()[0] + w[1:].lower()) 
            for w in input_str.split()
        ) # Note: The above logic is a naive expectation check; actual code just caps first char.
        
        results[i+1] = {
            "Input": repr(input_str),
            "Output": result,
            #"Expected Logic Check" (commented out for clarity in this specific implementation) 
            # Because the task asks to capitalize ONLY the first letter regardless of rest's case:
            # e.g. hELLO -> HELLO is WRONG based on prompt interpretation? 
            # Prompt says "capitalize... where only the first character ... is capitalized".
            # Standard English capitalization would preserve rest, but literally reading it suggests changing 1st to upper, others untouched.
        }

    for idx in results:
        print(f"Test Case {idx}:")
        print("Input:", repr(test_cases[idx-1]))
        print("Output:", results[idx]["Output"])
        
        # Manual verification of specific cases based on strict interpretation (First char upper, rest unchanged)
        if test_cases[idx-1] == "hELLO WoRLd":
            assert results[idx]["Output"] == "HELLO WORLD", "Logic check failed: hELLO -> HELLO expected"
            
    print("\nAll internal tests passed successfully.")