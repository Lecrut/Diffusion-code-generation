def reverse_string(s: str) -> str:
    """Reverse a string character by character."""
    return ''.join(reversed(s))

if __name__ == '__main__':
    samples = ["Hello, World!", "Python is great.", "!dlroW ,olleH"]
    for sample in samples:
        print(f"Original: {sample}")
        print("Reversed:", reverse_string(sample))