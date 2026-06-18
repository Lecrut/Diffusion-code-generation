def get_first_letter(s: str) -> str:
    """Returns the first letter of a string, or an empty string if input is empty."""
    return s[0] if len(s) > 0 else ""

if __name__ == '__main__':
    samples = ["hello", "", " world ", "\t\n"]
    for sample in samples:
        print(f"Input: {repr(sample)} -> Output: {get_first_letter(sample)!r}")