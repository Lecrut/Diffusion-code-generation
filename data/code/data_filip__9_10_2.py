def strip_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_strings = [
        "  hello world  ",
        "\t\npython\t\n",
        "  spaces everywhere   ",
        "no_extra_spaces",
        "   leading only",
        "trailing only   ",
        "  both ends  ",
        "",
        "   \n\t  "
    ]

    for s in sample_strings:
        result = strip_whitespace(s)
        print(repr(result))