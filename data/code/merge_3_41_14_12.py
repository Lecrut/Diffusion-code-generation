import unicodedata
from typing import Callable

def _is_alphabetic(char: str) -> bool:
    """Check if a character is alphabetic using Unicode categories."""
    return char.isalpha() and not char.isdigit()

def to_lowercase(text: str, strict_ascii_fallback: bool = False) -> str:
    """
    Convert string to lowercase.

    Uses Python's built-in string method which is highly optimized (C-level).
    Handles Unicode characters correctly for most locales unless specific constraints apply.
    
    Args:
        text (str): The input string.
        
    Returns:
        str: Lowercase version of the input string.
    """
    return text.lower()

def to_uppercase(text: str, strict_ascii_fallback: bool = False) -> str:
    """
    Convert string to uppercase.

    Uses Python's built-in string method which is highly optimized (C-level).
    
    Args:
        text (str): The input string.
        
    Returns:
        str: Uppercase version of the input string.
    """
    return text.upper()

def to_title_case(text: str, strict_ascii_fallback: bool = False) -> str:
    """
    Convert string to title case (first letter of each word capitalized).

    Uses Python's built-in string method which is optimized and handles Unicode well.
    
    Args:
        text (str): The input string.
        
    Returns:
        str: Titlecase version of the input string.
    """
    return text.title()

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    samples = [
        "hello world",
        "Python 3 Programming",
        "café résumé naïve",
        "",
        "   multiple     spaces   ",
        "ALL CAPS TEST!",
        "Mixed CASE 123 Numbers"
    ]

    print("Original | Lowercase | Uppercase | Titlecase")
    print("-" * 70)

    for sample in samples:
        lower = to_lowercase(sample)
        upper = to_uppercase(sample)
        title = to_title_case(sample)
        
        # Ensure no trailing newline issues from print formatting if needed, 
        # though standard str repr handles it.
        result_str = f"{sample!r} | {lower!r} | {upper!r} | {title!r}"
        print(result_str)

    # Additional specific verification for edge cases mentioned in requirements
    test_cases = [
        ("a", "A"),
        ("B", "b"),
        ("ABC def GHI", "Abc Def Ghi")
    ]

    print("\nVerification of function logic:")
    all_passed = True
    
    for input_val, expected_lower in to_lowercase: # This is just illustrative; actual usage follows below manually if needed. 
       pass 

    manual_check_cases = [
        ("hello", "HELLO"),
        ("WORLD", "world")
    ]

    print("\nDetailed Logic Check:")
    for inp, expected_lower in test_cases: # Actually iterating through the defined list above is better logic flow
    
        lower_res = to_lowercase(inp)
        upper_res = to_uppercase(inp)
        title_res = to_title_case(inp)
        
        status_l = "PASS" if lower == inp.lower() else f"Fails (got {lower})" 
        # Re-calculation for clarity in this specific block execution
        
    print("-" * 70)
    
    final_demo_input = "Hello, World! This is a TEST."
    print(f"\nDemo Input: {final_demo_input}")
    print(f"To Lowercase:   '{to_lowercase(final_demo_input)}'")
    print(f"To Uppercase:   '{to_uppercase(final_demo_input)}'")
    print(f"To Title Case:  '{to_title_case(final_demo_input)}'")