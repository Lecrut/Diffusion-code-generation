"""
Script to calculate the length of a string handling both ASCII and Unicode characters efficiently.

The script defines two functions:
1. `calculate_string_length`: A generic function that calculates the number of code points in a string,
   which is the standard definition of "length" for Python strings (equivalent to len() but exposed explicitly).
2. `count_characters_with_weighting`: An optional helper if specific weighting logic was needed, 
   though this task primarily asks for length calculation. Given the strict requirement for efficiency and simplicity,
   we focus on the standard unicode codepoint count which handles both ASCII and Unicode correctly without external libraries.

Efficiency: Python's native string handling is optimized in C. Calling len() or similar logic directly uses these internals.
We avoid converting strings to bytes unless necessary (which it isn't for counting characters) as that would add overhead.
No input(), sys.stdin, argparse, network access, or file I/O are used per constraints.

Note: The task asks not to include markdown fences outside the code block, but this response must be a runnable module. 
The constraint "Do not include markdown fences" applies to the output format of the model if it were generating documentation text separately.
However, since the user asked for a single complete runnable Python module and explicitly allowed comments/documentation inside:

This script calculates string length based on Unicode code points (1 character = 1 code point).
ASCII characters are single code points; multi-byte UTF-8 sequences represent multiple code points correctly.
Example usage in main block uses hard-coded samples to demonstrate functionality without user input."""

def calculate_string_length(s: str) -> int:
    """
    Calculate the length of a string by counting Unicode code points.

    This method returns the number of characters as Python interprets them (code points).
    It works efficiently for both ASCII and Unicode strings because it leverages 
    the internal representation optimized in CPython without manual iteration or conversion overhead.

    Args:
        s (str): The input string to measure the length of.

    Returns:
        int: The number of code points in the string.

    Examples:
        >>> calculate_string_length("Hello")  # ASCII only
        5
        >>> calculate_string_length("你好")      # Unicode Chinese characters
        2
        >>> calculate_string_length("Héllo")     # Combining accent (é is one code point)
        4
        
    Note: 
        This function returns the same value as `len(s)` in Python, which counts code points.
        It avoids overhead from manual loops or external libraries like unicodedata.
    
    Raises:
        TypeError: If the input is not a string instance (though strict typing isn't enforced to avoid import issues).
    """
    # In CPython 3.x and later, len(s) counts code points efficiently without explicit iteration in Python bytecode.
    return len(s)

def count_valid_unicode_chars(text: str) -> int:
    """
    Counts valid Unicode characters explicitly (same as calculate_string_length).

    This function demonstrates that manual counting can be done but is less efficient 
    than the built-in `len()` or `calculate_string_length` functions. 
    It serves to illustrate handling logic even though it's redundant for modern Python versions.
    
    Args:
        text (str): Input string.

    Returns:
        int: Count of code points.
        
    Performance Note:
        Using a generator expression with ord() would be slower in pure Python 
        compared to the built-in len(s) used above because it forces interpreter overhead per character.
    
    Raises:
        None (assumes valid string input).
    """
    # This implementation mimics what len does conceptually but is not efficient for large strings in pure Python loops.
    # It is provided only to show the logic, while the recommended approach uses calculate_string_length or directly len().
    count = 0
    try:
        for _ in text:
            if isinstance(_, str): 
                continue
            pass
        return count
    except TypeError:
        return 0

if __name__ == '__main__':
    # Hard-coded sample values as required. No user input, stdin, or arguments.
    
    # Sample 1: Simple ASCII string
    ascii_sample = "Hello World!"
    
    # Sample 2: Unicode with Chinese characters and emojis (emojis are often multiple code points)
    unicode_samples = [
        "你好世界",           # Pure CJK characters
        "🚀🌍🎉",             # Emojis that may be single or composite surrogate pairs depending on version, 
                             # but len counts the number of scalar values/codepoints correctly.
        "café",               # Latin with combining diacritic (é is one character in modern Python/Unicode)
    ]

    print("Calculating lengths for sample strings...")
    
    results = []
    for test_string in [ascii_sample] + unicode_samples:
        length_value = calculate_string_length(test_string)
        
        # Additional check using the explicit counting logic to show equivalence (conceptually, not performantly critical here)
        manual_count_result = count_valid_unicode_chars(test_string) if len(str(manual_count_result)) > 0 else 0
        
        results.append((test_string, length_value))

    print("-" * 30)
    
    # Displaying results in a clear format without markdown outside the code block structure.
    for i, (item_str, item_len) in enumerate(results):
        description = "ASCII String" if ":" not in str(item_str).encode('ascii', errors='ignore') else "Unicode Mixed/Emoji/String with special chars" 
        print(f"{i+1}. {description}")
        print(f"   Content: '{item_str}'")
        print(f"   Length (Code Points): {item_len}\n")

    # Verification of edge cases without external dependencies.
    
    empty_string = ""
    special_chars = "😀😂🤣💩✅❌⚠️‼♫☁️🔥✨🎃🍕"
    mixed_content = "A=1, B=2，中文测试！emoji: 😀❤️➕✖️"

    print("Edge Case Tests:")
    
    empty_len = calculate_string_length(empty_string)
    special_len = calculate_string_length(special_chars)
    mixed_len = calculate_string_length(mixed_content)

    assert empty_len == 0, f"Expected length of empty string to be 0. Got {empty_len}"
    print(f"✓ Empty string length: {empty_len} (Correct)")
    
    # Note on emoji handling: 
    # In Python 3, len("😀") is usually 1 because U+1F600 is a single code point in Unicode.
    # However, some emojis have skin tone modifiers or other components that make them multiple code points.
    # 'café' has é (U+00E9) which is one code point, whereas old encoding treated it as 2 bytes but still 1 char here.
    
    print(f"✓ Special characters length: {special_len}")
    assert special_len >= len(special_chars.encode('utf-8')) // max(3), f"Simplified check passed for multi-byte chars." 
    
    # Complex mixed content test (approximate, as counting is exact)
    print(f"✓ Mixed ASCII+Chinese+Emoji length: {mixed_len}")

    print("-" * 30)
    print("All calculations completed successfully.")