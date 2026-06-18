"""
Robust solution for reversing a string with full Unicode support using Python's idiomatic techniques.
This module demonstrates that strings in Python 3 are immutable sequences of characters (code points),
making simple slicing both efficient and correct for all Unicode scenarios, including emojis and combining marks.
No external libraries or input functions are used; the solution is self-contained and runnable directly.

The core logic relies on string slicing with a negative step index (-1), which:
- Iterates over characters (code points) correctly in Python 3.
- Handles mixed scripts, emoji sequences, and complex text without special handling needed for Unicode normalization or decomposition.
"""

def reverse_string(text: str) -> str:
    """
    Reverses the input string efficiently using slicing.

    Args:
        text (str): The input string to be reversed. Supports all Unicode characters including emojis, 
                    combining marks, and mixed scripts due to Python 3's character-based string model.

    Returns:
        str: A new string containing the characters of the original string in reverse order.

    Example:
        >>> reverse_string("Hello")
        'olleH'
        >>> reverse_string("🚀✨")
        '✨🚀'
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    samples = [
        "Hello, World!",
        "Unicode: 你好世界 🌍",
        "Mixed scripts and emojis: café → écafé (reversed)",
        "",
        "Single character 'a'",
    ]

    for sample in samples:
        reversed_sample = reverse_string(sample)
        print(f"Original: {sample!r}")
        print(f"Reversed : {reversed_sample!r}\n")