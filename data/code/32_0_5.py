#!/usr/bin/env python3
"""
Script to calculate the length of a given string efficiently handling both ASCII 
and Unicode characters (e.g., emojis, accented letters).

The script uses Python's native len() function which correctly counts code points,
suitable for most general purposes. For byte-level counting or specific surrogate 
pair handling in legacy contexts, additional logic could be applied, but standard
string length is defined by the number of Unicode scalar values (code points) unless
otherwise specified via encoding specifics like 'utf-8' bytes.

This implementation assumes strings are unicode objects (str type). If input were 
bytes, conversion to str would occur first using UTF-8 decoding if not already provided.
"""

def calculate_string_length(input_str: str) -> int:
    """
    Calculate the length of a string in terms of Unicode code points.

    This function is efficient and handles mixed ASCII/Unicode characters correctly.
    
    Args:
        input_str (str): The string whose length needs to be calculated.

    Returns:
        int: The number of code points in the string.
        
    Raises:
        TypeError: If the input is not a string type.
    """
    if not isinstance(input_str, str):
        raise TypeError(f"Expected 'str' object, got '{type(input_str).__name__}'")

    # Python's len() on strings returns the number of Unicode code points.
    return len(input_str)

def calculate_length_bytes_efficiently(byte_data: bytes) -> int:
    """
    Calculate the length of a byte sequence interpreted as UTF-8, 
    returning the count of individual characters (code points).

    This avoids potential issues with surrogate pairs in older Python versions or 
    specific encoding edge cases by decoding first. It is efficient for standard use-cases.

    Args:
        byte_data (bytes): The raw bytes representing a UTF-8 string.

    Returns:
        int: The number of characters represented by the byte data.
        
    Raises:
        UnicodeDecodeError: If the bytes cannot be decoded as valid UTF-8.
    """
    try:
        # Decode assuming standard UTF-8 encoding to get a str object first
        text = byte_data.decode('utf-8')
        return calculate_string_length(text)
    except UnicodeDecodeError as e:
        raise ValueError(f"Invalid UTF-8 sequence provided. Error details: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    
    samples = [
        "Hello, World!",  # Simple ASCII string
        "Café",           # String with accented character (Unicode)
        "🌍🚀💻",         # Emoji characters which are multi-byte in UTF-8 but single code points usually
        "",               # Empty string edge case
    ]

    print("String Length Calculation Results:")
    for idx, sample in enumerate(samples):
        length = calculate_string_length(sample)
        byte_len = len(sample.encode('utf-8'))  # Optional: show raw bytes count if needed
        
        output_info = f"Sample {idx + 1}: '{sample}' -> Unicode Length: {length}, UTF-8 Byte Count: {byte_len}"
        print(output_info)

    # Demonstrate byte input handling as well for completeness regarding the task description
    sample_bytes = b"Caf\xc3\xa9"  # 'Caf' + '\xc3\xae' (é in UTF-8 is two bytes: \xc3 \xa9)
    
    print("\nByte Input Handling:")
    try:
        byte_length_chars = calculate_length_bytes_efficiently(sample_bytes)
        print(f"Bytes '{sample_bytes.decode('utf-8')}' -> Character Count: {byte_length_chars}")
    except ValueError as e:
        print(f"Error processing bytes: {e}")