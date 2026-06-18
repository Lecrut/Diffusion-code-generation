def reverse_string(s: str) -> str:
    """
    Reverses a string efficiently using Python's built-in slicing,
    which handles Unicode characters correctly out of the box.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Sample values covering ASCII, mixed case, digits, and various Unicode characters including emojis and CJK
    test_cases = [
        "Hello World",
        "Python 3.9 is awesome!",
        "Unicode: 🌍🚀✅✨",
        "日本語テスト：ABC",
        "",
        "A" * 100,
        "Mixed: \u267b\u25ba\ud83d\udd2f"
    ]

    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        print(f"Original:   {test_input}")
        print(f"Reversed:   {reversed_output}")
        print("-" * 40)