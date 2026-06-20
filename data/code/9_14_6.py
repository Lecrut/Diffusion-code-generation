def strip_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_strings = [
        "   Hello, World!   ",
        "\t\n  Python  \r\n",
        "No whitespace here",
        "    ",
        "",
        "   Leading and trailing   "
    ]
    for s in sample_strings:
        print(strip_whitespace(s))