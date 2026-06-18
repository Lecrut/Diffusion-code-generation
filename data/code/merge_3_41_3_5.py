def process_string(s: str) -> tuple[str, str, str]:
    """
    Returns a tuple with three strings derived from the input string s:
    1. The original string.
    2. The lowercase version of the string.
    3. A new string where all characters are reversed in case (uppercase becomes lowercase and vice versa).

    Args:
        s (str): The input string to process.

    Returns:
        tuple[str, str, str]: A tuple containing (original_string, lower_case_string, reverse_case_string).
    """
    original = s
    lower_version = s.lower()
    
    # Create a mapping for case reversal using built-in methods and dictionary comprehension logic implicitly via string operations
    def char_to_reverse_char(c: str) -> str:
        if c.isupper():
            return chr(ord('a') + ord(c) - ord('A'))
        elif c.islower():
            return chr(ord('A') + ord(c) - ord('a'))
        else:
            # Non-alphabetic characters remain unchanged as per standard case reversal logic usually applied to text, 
            # though the prompt implies focusing on 'case'. Assuming non-alpha chars stay same.
            return c

    reverse_case_chars = [char_to_reverse_char(c) for c in s]
    reversed_case_string = ''.join(reverse_case_chars)

    return original, lower_version, reversed_case_string

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_input_1 = "Hello World!"
    result_1 = process_string(test_input_1)
    
    test_input_2 = "Python3.9"
    result_2 = process_string(test_input_2)

    print(f"Input: '{test_input_1}'")
    print(f"Result Tuple 1: {result_1}")
    # Unpacking for clarity in output demonstration if needed, but tuple is the return value requirement.
    
    print("\n--- Next Sample ---\n")
    print(f"Input: '{test_input_2}'")
    print(f"Result Tuple 2: {result_2}")