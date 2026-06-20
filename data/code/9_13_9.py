def trim_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    samples = [
        "  hello world  ",
        "\t\n  spaces and tabs  \n\t",
        "no_trim_needed",
        "   ",
        "",
        "  leading",
        "trailing  ",
    ]
    for sample in samples:
        print(repr(trim_whitespace(sample)))