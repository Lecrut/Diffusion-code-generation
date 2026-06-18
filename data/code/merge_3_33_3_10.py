import string

def remove_spaces(s: str) -> str:
    """Remove all spaces from a given string."""
    return "".join(c for c in s if not (c == ' ' or c in '\t\n\r'))

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "\t\tPython 3.10 \n ",
        string.ascii_letters + "",
        ""
    ]
    for case in test_cases:
        print(remove_spaces(case))