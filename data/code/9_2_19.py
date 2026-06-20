def trim_whitespace(strings):
    return [s.strip() for s in strings]

if __name__ == '__main__':
    sample_strings = [
        "  hello world  ",
        "\t\ttest\t\t",
        "\nnewlines\n",
        "   spaces   ",
        "no_extra"
    ]
    result = trim_whitespace(sample_strings)
    print(result)