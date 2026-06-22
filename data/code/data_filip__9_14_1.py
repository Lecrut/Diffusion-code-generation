def strip_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    samples = [
        "  hello world  ",
        "\t\n hello \n\t",
        "",
        "   ",
        "no_whitespace_here",
        "  mixed   spaces   here  "
    ]
    for sample in samples:
        print(strip_whitespace(sample))