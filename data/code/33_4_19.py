def clean_string(s: str) -> str:
    """
    Returns a new string containing only alphanumeric characters from the input.
    
    All spaces, punctuation marks, symbols, and other non-alphanumeric 
    characters are filtered out. The original casing is preserved for valid 
    letters while digits remain unchanged.

    Args:
        s (str): The input string to process.

    Returns:
        str: A cleaned string with only alphanumeric characters.
    """
    result = []
    
    # Iterate over each character in the string
    for char in s:
        if char.isalnum():
            result.append(char)
            
    return ''.join(result)

if __name__ == '__main__':
    sample_1 = "Hello, World! How are you? 2024."
    cleaned_result = clean_string(sample_1)
    
    # Verify the function works as expected on multiple scenarios
    test_cases = [
        ("aBcD eFG", "abcdegf"),
        ("123 ! @# $%^&*()", ""),
        (" ", ""),
        ("No special chars here!", "Nospecialcharshere")
    ]

    print(f"Sample 1 Input: {sample_1}")
    print(f"Cleaned Output: {cleaned_result}\n")
    
    for i, (input_str, expected) in enumerate(test_cases):
        output = clean_string(input_str)
        status = "PASS" if output == expected else f"FAIL (Expected: '{expected}', Got: '{output}')"
        print(f"Test Case {i+1}: Input='{input_str}' -> Output='{output}' - Status: {status}")

    # Ensure the module is runnable without any external dependencies or prompts