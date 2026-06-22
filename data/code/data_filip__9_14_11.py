def remove_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    samples = [
        "  hello world  ",
        "\t\n\r  spaces  \r\n\t",
        "",
        "no_whitespace",
        "\n\n\n",
        " leading_only",
        "trailing_only ",
        "  both sides  ",
    ]
    for sample in samples:
        result = remove_whitespace(sample)
        print(repr(result))