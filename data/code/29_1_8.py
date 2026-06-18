def reverse_word(s: str) -> str:
    """Returns a new string with characters in 's' reversed using slicing."""
    return s[::-1]

if __name__ == '__main__':
    samples = ["hello", "Pythonic!", "", "a"]
    for sample in samples:
        print(f"Original: '{sample}' -> Reversed: '{reverse_word(sample)}'")