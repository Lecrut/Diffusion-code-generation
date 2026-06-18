def reverse_string(s: str) -> str:
    """Reverses a string by slicing it backwards."""
    return s[::-1]

if __name__ == '__main__':
    sample_inputs = ["hello", "Python"]
    for inp in sample_inputs:
        print(f"Original: {inp}, Reversed: {reverse_string(inp)}")