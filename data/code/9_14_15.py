def strip_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_strings = [
        "  hello world  ",
        "\t\n  python  \n\t",
        "no_whitespace",
        "   ",
        "",
        "  leading",
        "trailing  "
    ]
    for s in sample_strings:
        print(repr(strip_whitespace(s)))