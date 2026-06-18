"""
Robust string reversal solution using Python's most efficient built-in capabilities.
Correctly handles Unicode characters (including emojis, non-Latin scripts, etc.)
by leveraging C-optimized internal methods rather than character-by-character loops.
"""

def reverse_string(text: str) -> str:
    """
    Reverses the input string efficiently and correctly for all Unicode characters.

    Args:
        text (str): The string to be reversed. Can contain any valid Python unicode characters.

    Returns:
        str: A new string with the characters in reverse order, preserving original encoding/unicode semantics.

    Efficiency Note:
        This function uses slicing (`[::-1]`), which is implemented in C and handles 
        all Unicode code points (including surrogate pairs for emojis) correctly without explicit loops.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality with various unicode cases
    samples = [
        "Hello, World!",  # Basic ASCII and punctuation
        "🌍Python3",       # Emojis mixed with Latin script
        "日本語テスト",     # Japanese characters (surrogates handled natively)
        "Café naïve résumé", # Accented characters from French/Unicode norms
    ]

    for sample in samples:
        reversed_sample = reverse_string(sample)
        print(f"Original:  {sample}")
        print(f"Reversed:  {reversed_sample}\n")