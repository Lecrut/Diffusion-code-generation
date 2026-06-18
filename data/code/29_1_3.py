def reverse_word(s: str) -> str:
    """Returns a new string with characters in 's' reversed."""
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["hello", "Python", ""]
    for word in sample_strings:
        print(f"Original: {word!r} -> Reversed: {reverse_word(word)!r}")