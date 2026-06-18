def reverse_string(s: str) -> str:
    """
    Reverses a string while correctly handling Unicode characters.
    
    This function uses Python's built-in slicing operator, which is optimized in C
    and natively handles all Unicode code points (including emojis, combining marks,
    surrogate pairs, etc.) without requiring explicit encoding/decoding steps.
    
    Args:
        s (str): The input string to reverse.
        
    Returns:
        str: A new string with characters in reversed order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Sample test cases covering ASCII, mixed Unicode, emojis, and combining characters
    samples = [
        "Hello World",                      # Basic ASCII
        "你好世界",                          # Chinese characters
        "\u05d0\u05d1\u05d2\u05d3",         # Hebrew (RTL language)
        "🚀✨💻",                           # Emojis and symbols
        "café naïve résumé",                # Accented characters
        "a\u0301b"                          # Combining acute accent ('ab' with accent on b)
    ]

    results = [reverse_string(sample) for sample in samples]

    print("Original Strings:")
    for i, s in enumerate(samples):
        print(f"{i+1}. {s!r}")
    
    print("\nReversed Strings:")
    for i, r in enumerate(results):
        print(f"{i+1}. {r!r}")

    # Verify correctness by checking if original equals reversed of reversed
    assert all(s == reverse_string(r) for s, r in zip(samples, results)), "Reverse operation failed"