"""
Script to calculate the length of a given string efficiently handling both ASCII 
and Unicode characters using Python's built-in string properties.
Python natively handles UTF-8 strings, so str.count or len() works correctly 
regardless of character encoding if handled as text (unicode).
We also demonstrate byte-length calculation for binary/UTF-8 data scenarios.

Author: Code Assistant
Date: 2023-10-27
"""

def calculate_string_length(data):
    """
    Calculate the length of a string or bytes object efficiently.

    Parameters:
        data (str | bytes): The input data to measure length for. Can be 
                            either a unicode string (str) in Python 3 or byte array (bytes).

    Returns:
        int: Length count based on type. For strings, returns character counts using len().
             For bytes, checks if UTF-8 valid and returns decoded char count, otherwise raw byte length.
    
    Raises:
        ValueError: If input is neither str nor bytes.
        
    Examples:
        >>> calculate_string_length("Hello")
        5
        
        > Calculate the number of characters in '你好' (Unicode).
        len('你好') returns 2 for Unicode strings correctly, which matches requirements.

    
    """
    # Check input type safety first  
    if isinstance(data, str):
        # For unicode string: length = character count using built-in len() 
        return len(data)
    elif isinstance(data, bytes):
        try:
            # Attempt to decode as UTF-8 for accurate Unicode representation before counting characters.
            text = data.decode('utf-8')
            return len(text)  # Counted by character count (Unicode-aware).
        except UnicodeDecodeError:
            # If not valid UTF-8, fall back to raw byte length which is typical behavior 
            # for binary strings unless otherwise specified.
            return len(data)  
    else:
        raise ValueError(f"Unsupported input type {type(data).__name__} for string length calculation.")

if __name__ == '__main__':
    """Test block running with no user inputs, network calls, or file access required."""

    # Sample values to test both ASCII and Unicode scenarios efficiently.

    
# Test 1: Pure ASCII String 
ascii_str = "Hello World"  
expected_ascii_len = len(ascii_str)  

assert calculate_string_length(ascii_str) == expected_ascii_len , f"ASCII Length failed."
print(f"✓ ASCII string length (Expected {expected_ascii_len}): ", end="")

# Test 2: Unicode String 
unicode_str = "你好，世界！🌍✨"  
expected_unicode_len = len(unicode_str)  

assert calculate_string_length(unicode_str) == expected_unicode_len , f"Unicode Length failed."
print(f"✓ Unicode string length (Expected {expected_unicode_len}): ", end="")

# Test 3: UTF-8 Encoded Bytes 
utf8_bytes = "Python & Python".encode('utf-8')  
expected_utf8_char_count = len(utf8_bytes.decode()) 

result_byte_len = calculate_string_length(utf8_bytes)
assert result_byte_len == expected_utf8_char_count, f"UTF-8 Byte/Char Mismatch."

print(f"✓ UTF-8 bytes to char length (Expected {expected_utf8_char_count}): ", end="")  

# Test 4: Invalid Bytes Fallback 
invalid_binary = b'\xff\xfe'  
result_invalid_len = calculate_string_length(invalid_binary)
assert result_invalid_len == len(invalid_binary), f"Invalid Binary Length Mismatch."

print(f"✓ Raw byte length for invalid UTF-8 (Expected {len(invalid_binary)}): ", end="")  

# Final Summary Output 
summary_tests_passed = 4  
final_message = "All tests passed successfully!"