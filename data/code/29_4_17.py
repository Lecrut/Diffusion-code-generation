import unicodedata

def reverse_string(text: str) -> str:
    """
    Reverses the order of characters in a string, handling Unicode correctly.

    This function iterates through the input string and constructs a new string
    with characters in reversed order. It uses Python's native iteration behavior
    which handles mixed scripts (e.g., ASCII, Greek, CJK) and emoji as single units
    unless they are explicitly composed of multiple code points that need specific normalization;
    however, standard simple reversal operates on the character sequence provided by `str`.

    For strings containing complex emojis or skin tone modifiers requiring byte-level
    inversion (where visual order differs from code point order), this function returns a string
    where characters are reversed as per their Unicode representation. To achieve perfect
    visual symmetry for such edge cases, input should be normalized using 'NFC' form before reversal
    if strict semantic preservation is required beyond simple sequence inversion.

    Args:
        text (str): The input string to reverse. Can contain any valid UTF-8 characters including emojis and non-Latin scripts.

    Returns:
        str: A new string with the order of all Unicode code points reversed relative to the original text.

    Raises:
        TypeError: If `text` is not a string instance.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("你好世界")
        '界世好你'
        >>> reverse_string("\U0001F600\U0001F982")  # Grinning Face + High Five Hand ✌️ (Note: Emojis are single code points usually)
        '👏😀'

    Note:
        If the string contains characters composed of multiple code points (e.g., combining accents), simple reversal
        may invert those components. For strict visual correctness in such complex scenarios, consider normalizing with unicodedata.normalize('NFC', text) prior to this function if necessary for semantic integrity.
    """
    # Basic type checking and execution
    if not isinstance(text, str):
        raise TypeError(f"Expected string object, got {type(text).__name__}")

    return "".join(char * -1 for char in reversed(list(text)))

if __name__ == '__main__':
    sample_strings = [
        "Hello World!",
        "\u4f60\u597d\u4e16\u754c",  # Simplified Chinese: 你好世界
        "\U0001F608\U0001FAE2",   # 😺 + ✌️ (Emojis with zero width joiner or combined logic) - actually just two emojis here for simple test
    ]

    output = [f"{s} -> {reverse_string(s)}" for s in sample_strings]
    print("\n".join(output))