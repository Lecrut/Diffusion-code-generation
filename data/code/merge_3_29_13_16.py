def reverse_string(s: str) -> str:
    """Reverses a string efficiently."""
    return s[::-1]

if __name__ == '__main__':
    samples = ["hello", "Python is great!", "", "a"]
    for sample in samples:
        print(f"Original: {sample}, Reversed: {reverse_string(sample)}")