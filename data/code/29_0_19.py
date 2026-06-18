import sys

def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string efficiently using slicing.
    
    Args:
        input_str (str): The string to be reversed. Handles empty strings, Unicode characters, and special symbols correctly.
        
    Returns:
        str: A new string that is the reverse of the input string.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test various edge cases without user interaction or external dependencies
    
    samples = [
        "",                      # Empty string
        "Hello, World!",        # Standard sentence with punctuation and spaces
        "!@#$%^&*()",            # Special characters
        "Unicode: 你好世界 🌍",   # Unicode text including emoji
        "1234567890",           # Numeric digits only
    ]
    
    for sample in samples:
        reversed_str = reverse_string(sample)
        print(f"Input:    '{sample}'")
        print(f"Reversed: '{reversed_str}'")
        print("-" * 30)