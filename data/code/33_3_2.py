def remove_spaces(s: str) -> str:
    """Remove all spaces from a string."""
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "Competitive Programming is Fun!",
        "",
        "   Multiple   Spaces   Here   ",
        "NoSpacesHere"
    ]
    for case in test_cases:
        print(f"Input: {case!r} -> Output: {remove_spaces(case)!r}")