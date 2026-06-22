def trim_spaces(s):
    return s.strip()

if __name__ == '__main__':
    sample = "  hello world  "
    print(trim_spaces(sample))
    sample2 = "\t\n  foo bar \n\t"
    print(trim_spaces(sample2))
    sample3 = "no_spaces"
    print(trim_spaces(sample3))