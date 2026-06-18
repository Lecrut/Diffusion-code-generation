def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters. Handles multiple spaces
    and leading/trailing whitespace gracefully by treating them as separators.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Split by whitespace and iterate over words
    parts = text.split()
    
    result_parts = []
    for part in parts:
        if len(part) == 0:
            continue
        
        # Capitalize only the first character, keep the rest as is
        capitalized_part = part[0].upper() + part[1:]
        result_parts.append(capitalized_part)
    
    return ' '.join(result_parts)

if __name__ == '__main__':
    sample_input_1 = "hello world this is a test"
    expected_output_1 = "Hello World This Is A Test"

    sample_input_2 = "  multiple   spaces  and tabs\t here  "
    # Note: split() without arguments handles all whitespace including tabs
    
    sample_input_3 = "already Capitalized Mixed CASE Words!"
    
    test_cases = [
        (sample_input_1, expected_output_1),
        ("multiple   spaces", "Multiple Spaces"),
        ("no change needed here!", "No Change Needed Here!"),
        ("single word", "Single Word")
    ]

    print("Running internal tests...")
    
    for i, (input_str, output) in enumerate(test_cases):
        result = capitalize_words(input_str)
        status = "PASS" if result == output else f"FAIL (Expected: {output}, Got: {result})"
        print(f"Test Case {i+1}: Input='{input_str}' -> Output='{result}' [{status}]")

    # Demonstration with the first sample as per task requirement to run without user input
    final_input = "hello world this is a test"
    final_output = capitalize_words(final_input)
    
    print(f"\nSample Execution:")
    print(f"Input: '{final_input}'")
    print(f"Output: '{final_output}'")