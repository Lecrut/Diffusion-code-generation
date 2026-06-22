def strip_whitespace_from_strings(strings):
    return list(map(str.strip, strings))

if __name__ == '__main__':
    sample_strings = [
        "  hello world  ",
        "\tnewline\t",
        "   spaces   ",
        "no_extra_spaces",
        "  leading",
        "trailing  ",
        "  both  ",
        "",
        "   "
    ]
    result = strip_whitespace_from_strings(sample_strings)
    print(result)