import re

def remove_spaces(s: str) -> str:
    """Remove all spaces from a string efficiently."""
    return "".join(c if not c == ' ' else '' for c in s) or ""

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external input is needed
    test_strings = [
        "Hello World",
        "  Leading spaces here,   and trailing space!",
        "",           # Empty string edge case
        "NoSpacesHereAtAll"
    ]
    
    for original in test_strings:
        result = remove_spaces(original)
        print(f"Input:     '{original}'")
        print(f"Output:    '{result}'\n")