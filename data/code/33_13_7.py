def remove_spaces(s: str) -> str:
    """Returns a new string with all spaces removed."""
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = ["hello world", "  multiple   spaces  ", "no spaces here"]
    for case in test_cases:
        print(f"Input: {case!r} -> Output: {remove_spaces(case)!r}")