def reverse_word(text: str) -> str:
    """Returns the reversed string."""
    return text[::-1]

if __name__ == '__main__':
    sample_strings = ["hello", "Python is fun", ""]
    for s in sample_strings:
        print(f"Original: {s!r}")
        print(f"Reversed:{reverse_word(s)!r}\n")