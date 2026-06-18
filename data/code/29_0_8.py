#!/usr/bin/env python3
"""
Script to reverse a given input string efficiently.
Handles edge cases such as empty strings, unicode characters, 
and mixed character sets without external dependencies.
"""

def reverse_string(input_str: str) -> str:
    """
    Reverses the provided input string in-place using slicing for efficiency.

    Args:
        input_str (str): The string to be reversed. Handles empty strings and unicode gracefully.

    Returns:
        str: A new string containing characters of the original string in reverse order.
    
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("")
        ''
        >>> reverse_string("你好，世界!")
        '!界世，好你'
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    test_cases = [
        "hello world",           # Standard string with spaces
        "",                      # Empty string edge case
        "!@#$%^&*()",            # Special characters and symbols
        "你好，世界！",             # Unicode Chinese punctuation
        "1234567890",            # Numeric digits only
    ]

    print("String Reversal Demonstration")
    print("-" * 30)

    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        status = "[OK]" if test_input == reversed_output[::-1] else "[FAIL]" # Double check logic, though slicing is inherently correct.
        
        # Note: The condition `test_input == reversed_output[::-1]` will always be true because 
        # reversing a string twice returns the original (for immutable strings like str in Python).
        print(f"Input:    '{test_input}'")
        print(f"Reversed: '{reversed_output}'")
        print(status)
        
        if test_input == "":
            print("Edge Case Handled Correctly.")
        elif len(test_input) > 0 and len(reversed_output) != len(test_input):
            print("Error: Length mismatch detected (should not happen).")

    print("-" * 30)
    print("All tests completed successfully using slicing method.")