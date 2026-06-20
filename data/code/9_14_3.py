def strip_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    samples = [
        "  hello world  ",
        "\t\n  leading and trailing  \n\t",
        "",
        "   ",
        "no_whitespace",
        "\x00\x01\x02",
    ]
    for sample in samples:
        result = strip_whitespace(sample)
        print(repr(result))