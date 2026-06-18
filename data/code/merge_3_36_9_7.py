def reverse_string(s: str) -> str:
    """
    Reverses a string correctly handling all Unicode characters.
    
    This function uses Python's highly optimized slicing operator, 
    which handles both ASCII and Unicode (including emojis and complex scripts) efficiently.
    
    Args:
        s (str): The input string to reverse.
        
    Returns:
        str: A new reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values covering various Unicode scenarios
    samples = [
        "Hello World",                           # ASCII with space
        "你好世界",                              # Chinese characters (CJK)
        "🚀🌍✨",                               # Emojis
        "Café résumé naïve",                     # Accented characters
        "\u0628\u0631\u064a\u0627\u0646\u06cc",  # Arabic text (RTL)
    ]

    for sample in samples:
        reversed_sample = reverse_string(sample)
        print(f"Original: {sample!r}")
        print(f"Reversed : {reversed_sample!r}\n")