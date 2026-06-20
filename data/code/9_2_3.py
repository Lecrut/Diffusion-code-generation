def trim_whitespace(strings):
    return [s.strip() for s in strings]

if __name__ == '__main__':
    sample_strings = [
        "  hello world  ",
        "\t\tpython\t\t",
        "   \n\n  \n  ",
        "no_extra_spaces",
        "  leading and trailing  "
    ]
    trimmed = trim_whitespace(sample_strings)
    print(trimmed)