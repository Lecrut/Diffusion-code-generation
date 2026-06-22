def trim_spaces(text):
    return text.strip()

if __name__ == '__main__':
    sample1 = "  hello world  "
    sample2 = "\t\nfoo\n\t"
    sample3 = "no_spaces"

    print(trim_spaces(sample1))
    print(trim_spaces(sample2))
    print(trim_spaces(sample3))