def reverse_string(text: str) -> str:
    """Reverses the input string using Python's native slicing capability."""
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive prompts or dependencies
    samples = ["hello", "Hello World!", "", "Python is fun"]

    for s in samples:
        reversed_s = reverse_string(s)
        print(f"Original: {s!r}")
        print(f"Reversed: {reversed_s!r}\n")