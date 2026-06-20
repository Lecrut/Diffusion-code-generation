def remove_leading_trailing_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_strings = [
        "   Hello World   ",
        "\t\nPython Programming\n\t",
        "NoWhitespaceHere",
        "    ",
        "",
        "   LeadingOnly",
        "TrailingOnly   "
    ]

    for s in sample_strings:
        result = remove_leading_trailing_whitespace(s)
        print(f"Input: {repr(s)} | Output: {repr(result)}")