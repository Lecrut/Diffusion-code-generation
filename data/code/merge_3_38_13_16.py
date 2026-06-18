def has_repeated_letters(s: str) -> bool:
    """Check if a string contains any repeated letters (case-insensitive)."""
    chars = [c.lower() for c in s if c.isalpha()]
    return len(chars) != len(set(chars))

if __name__ == '__main__':
    # Sample test cases with expected results
    samples = ["hello", "world!", "abcdef", "aAaa123"]
    
    for sample in samples:
        result = has_repeated_letters(sample)
        print(f"'{sample}': {result}")  # Expected: True, False, False, True