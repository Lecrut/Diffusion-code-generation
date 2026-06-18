def remove_spaces(s: str) -> str:
    """Return a new string with all whitespace characters removed."""
    return s.replace(" ", "") if isinstance(s, str) else ""

if __name__ == "__main__":
    test_cases = [
        "Hello World",
        "...   ...",
        "",
        "No spaces here!",
    ]

    for case in test_cases:
        result = remove_spaces(case)
        print(f"Input:  '{case}'")
        print(f"Output: '{result}'\n")