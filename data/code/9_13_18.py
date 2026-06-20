def trim_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    sample1 = "  hello world  "
    sample2 = "\t\nfoo\t\n"
    sample3 = "no_whitespace"
    sample4 = "   leading_only"
    sample5 = "trailing_only   "
    print(trim_whitespace(sample1))
    print(trim_whitespace(sample2))
    print(trim_whitespace(sample3))
    print(trim_whitespace(sample4))
    print(trim_whitespace(sample5))