def reverse_string(s: str) -> str:
    """Reverse the order of characters in a given ASCII string."""
    return s[::-1]

if __name__ == '__main__':
    samples = ["Hello, World!", "Python", "A"]
    for sample in samples:
        print(f"Original: {sample} -> Reversed: {reverse_string(sample)}")