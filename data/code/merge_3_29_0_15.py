import sys

def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string efficiently using slicing.
    
    Args:
        input_str (str): The string to be reversed. Handles empty strings, 
                         Unicode characters, and special symbols correctly.
        
    Returns:
        str: A new string containing the reverse of the input.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user interaction or file access is required
    test_cases = [
        "",                       # Edge case: Empty string
        "hello",                  # Basic alphabetic characters
        "!@#$%",                 # Special symbols and Unicode readiness
        "\u0435\u0441\u0442\u044c \u044e\u043d\u0438\u043a\u0430",  # Cyrillic characters
    ]

    for test in test_cases:
        result = reverse_string(test)
        print(f"Original:   '{test}'")
        print("Reversed:   '{result}'\n".format(result=result))