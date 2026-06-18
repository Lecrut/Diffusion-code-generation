def reverse_string(s: str) -> str:
    """Reverse a string by slicing it with step -1."""
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "Python", "!olleH"]
    for test_input in sample_strings:
        print(f"Input: {test_input!r} -> Output: {reverse_string(test_input)!r}")